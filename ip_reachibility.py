##############################################################################
# Script that will help you to check ICMP Reachibility for multiples devices #
# This version uses threading for concurrent execution.                      #
# Autor: Jose Rafael Guerra Gonzalez                                         #
##############################################################################

##################
# Import Section #
##################

import yaml
import time
import concurrent.futures
import json
import smtplib
import os
from scapy.all import IP, ICMP, sr
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##########################
# Global Vars definition #
##########################

IP_REACHIBILITY_FILENAME = "ip_address.yaml"

############################
# Email Var Config Section #
############################

# Sender Email Address
sender_email = ""

# Receiver Email Address
receiver_email = ""

# SMTP Server Address
smtp_server = ""

# SMTP Port
smtp_port = 25

####################
# Function Section #
####################

# Function that generate a HTML variable based on the ICMP Statistics Data
def generate_network_report_html(data):

    # HTML Auxilear Variable 
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <title>Network Reachability Analysis</title>
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                background-color: #f0f2f5;
                margin: 0;
                padding: 20px;
                color: #333;
            }}
            .container {{
                max-width: 900px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #1a237e;
                text-align: center;
                border-bottom: 2px solid #e0e0e0;
                padding-bottom: 15px;
                margin-top: 0;
            }}
            .ip-section {{
                background-color: #fafafa;
                border: 1px solid #e0e0e0;
                border-left: 5px solid #4a148c;
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 25px;
                transition: transform 0.2s;
            }}
            .ip-section:hover {{
                transform: translateY(-5px);
            }}
            h2 {{
                color: #4a148c;
                margin-top: 0;
                display: flex;
                align-items: center;
            }}
            h2 .icon {{
                margin-right: 10px;
            }}
            .stats-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-top: 15px;
            }}
            .stat-card {{
                background-color: #ffffff;
                padding: 15px;
                border-radius: 8px;
                border: 1px solid #e0e0e0;
                text-align: center;
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
            }}
            .stat-card p {{
                margin: 0;
                font-size: 14px;
                color: #666;
            }}
            .stat-card .value {{
                font-size: 24px;
                font-weight: bold;
                color: #1a237e;
                margin-top: 5px;
            }}
            .packets-info {{
                margin-top: 20px;
                padding: 15px;
                background-color: #e8eaf6;
                border-radius: 8px;
                display: flex;
                justify-content: space-around;
                align-items: center;
            }}
            .packets-info p {{
                margin: 0;
                font-weight: bold;
            }}
            .status-badge {{
                padding: 5px 10px;
                border-radius: 5px;
                color: white;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
            }}
            .status-success {{
                background-color: #2e7d32;
            }}
            .status-warning {{
                background-color: #ffa000;
            }}
            .status-error {{
                background-color: #c62828;
            }}
            .footer {{
                text-align: center;
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid #e0e0e0;
                color: #888;
                font-size: 12px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ICMP Health Report</h1>
            <p style="text-align: center; font-style: italic;">Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    """

    for item in data:
        ip_address = item.get("IP", "N/A")
        description = item.get("Description", "No Description")
        rtt_stats = item.get("RTT Statistics", {})
        packets = item.get("Packets", {})

        transmitted = packets.get("Packets Transmitted", 0)
        received = packets.get("Packets Received", 0)
        loss = packets.get("Packets Loss", 0)
        loss_percentage = (loss / transmitted) * 100 if transmitted > 0 else 0

        status_class = "status-success"
        status_text = "Reachable"
        if loss_percentage > 50:
            status_class = "status-error"
            status_text = "Unreachable"
        elif loss_percentage > 0:
            status_class = "status-warning"
            status_text = "Partial Loss"

        html_content += f"""
        <div class="ip-section">
            <h2><span class="icon">&#x1F4BB;</span>IP: {ip_address}</h2>
            <p style="color: #283593;">Description: {description}</p>
            <div class="stats-grid">
                <div class="stat-card">
                    <p>Min RTT</p>
                    <p class="value">{rtt_stats.get("Minimum", 0.0):.2f} ms</p>
                </div>
                <div class="stat-card">
                    <p>Avg RTT</p>
                    <p class="value">{rtt_stats.get("Average", 0.0):.2f} ms</p>
                </div>
                <div class="stat-card">
                    <p>Max RTT</p>
                    <p class="value">{rtt_stats.get("Maximum", 0.0):.2f} ms</p>
                </div>
                <div class="stat-card">
                    <p>Total RTT</p>
                    <p class="value">{rtt_stats.get("Total", 0.0):.2f} ms</p>
                </div>
            </div>
            <div class="packets-info2">
                <p>Status: <span class="status-badge {status_class}">{status_text}</span></p>
                <p>Packets Sent: {transmitted}</p>
                <p>Packets Received: {received}</p>
                <p>Packets Loss: {loss} ({loss_percentage:.1f}%)</p>
            </div>
        </div>
    """

    html_content += f"""
        <div class="footer">
            <p>Report generated by the ICMP Reachibility Script.</p>
        </div>
        </div>
    </body>
    </html>
    """

    return html_content

# Function that will send ICMP packets to a single IP Address and return a dictionary with the results
def ping_ip(ip_info, icmp_params):

    # Setting the ip_address var with the dictionary obtained in the file ip_address.yaml
    ip_address = ip_info['ip']

    # We print the results if the verbose is set to True

    if icmp_params.get('verbose', False):
        print(f"--- Pinging {ip_address} ({ip_info.get('description', 'No Description')}) ---")

    # Initialize stats for this IP
    rttMax, rttMin, rttAvg_total = 0.0, 65000.0, 0.0
    pcktRec, pcktTrans, pcktLoss = 0, 0, 0

    # Sending ICMP Packets based on params
    for counts in range(icmp_params.get('num_icmp_packages', 5)):

        # Adding 1 packet transmited to auxilear var
        pcktTrans += 1

        # Starting to measure the time for the RTT calculation
        start_time = time.time()

        # Send and receive a single packet
        ans, _ = sr(IP(dst=ip_address) / ICMP(), timeout=icmp_params.get('timeout', 2), verbose=False)

        # Stop measuring the time for RTT calculation
        end_time = time.time()

        if ans:

            # Adding 1 packet received to auxilear var
            pcktRec += 1

            rtt = (end_time - start_time) * 1000
            if rtt > rttMax: rttMax = rtt
            if rtt < rttMin: rttMin = rtt
            rttAvg_total += rtt

            if icmp_params.get('verbose', False):
                print(f"Reply from {ip_address}: icmp_seq={counts+1} time={rtt:.2f}ms")
        else:

            # Adding 1 packet lost to auxilear var
            pcktLoss += 1

            if icmp_params.get('verbose', False):
                print(f"Request timed out for {ip_address}: icmp_seq={counts+1}")

        # Optional delay between packets for a single host
        time.sleep(icmp_params.get('delay_inter_packages', 0))

    # Final calculations for this IP
    # If no packets were received, set Min RTT to 0
    if pcktRec == 0:
        rttMin = 0.0

    # Calculate average only on received packets to be accurate
    avg_rtt_calc = rttAvg_total / pcktRec if pcktRec > 0 else 0.0

    # Prepare the result dictionary
    result = {
        'IP': ip_address,
        'Description': ip_info['description'],
        'RTT Statistics': {
            'Minimum': round(rttMin, 2),
            'Average': round(avg_rtt_calc, 2),
            'Maximum': round(rttMax, 2),
            'Total': round(rttAvg_total, 2)
        },
        'Packets': {
            'Packets Transmitted': pcktTrans,
            'Packets Received': pcktRec,
            'Packets Loss': pcktLoss
        }
    }

    if icmp_params.get('verbose', False):

        # Print final stats for the IP Address
        print(f"\nStatistics for {ip_address}:")
        print(f"  Packets: Sent = {pcktTrans}, Received = {pcktRec}, Lost = {pcktLoss} ({ (pcktLoss/pcktTrans)*100 if pcktTrans > 0 else 0:.1f}% loss)")

        if pcktRec > 0:
            print(f"  RTT (ms): Minimum = {result['RTT Statistics']['Minimum']}, Maximum = {result['RTT Statistics']['Maximum']}, Average = {result['RTT Statistics']['Average']}\n")

    return result

# Function to read IPs from a yaml file and send ICMP them concurrently
# The function return a list of dictionaries with all the data feched
def ICMP_reachibility():
    try:
        with open(IP_REACHIBILITY_FILENAME, 'r') as ips_file:

            # Loading the yaml file into the variable config_data
            config_data = yaml.safe_load(ips_file)

            # Obtained the ICMP Parameters storage in the Config Data Var
            icmp_params = config_data.get('icmp', {})

            # Obtained the IP Address List storaged in the Config Data Var
            ip_list = config_data.get('ip_address', [])

            # If there is no IP Address detected in the ip_list var (list emptly) we exit the function
            if not ip_list:
                print("No IP addresses found in the YAML file.")
                return

            # List that will save the Statistics and Packets counters in a dict format
            all_results = []

            # Use ThreadPoolExecutor to manage concurrent threads
            with concurrent.futures.ThreadPoolExecutor(max_workers=len(ip_list)) as executor:

                # Submit each ping_ip call as a future
                future_to_ip = {executor.submit(ping_ip, ip_info, icmp_params): ip_info for ip_info in ip_list}

                # Process results as they are completed
                for future in concurrent.futures.as_completed(future_to_ip):

                    # For each IP, we generate a ICMP reachibility test
                    ip_info = future_to_ip[future]

                    try:

                        # We save the dictionary obtained by the ping_ip function
                        all_results.append( future.result())

                    except Exception as exc:
                        print(f"Error pinging {ip_info['ip']}: {exc}")

    except FileNotFoundError:
        print(f"Error: The file '{IP_REACHIBILITY_FILENAME}' was not found.")
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")

    return all_results

################
# Main Program #
################

if __name__ == '__main__':

    # Variable that will save all the ICMP Data obtained by the IP Address
    data_list = ICMP_reachibility()

    # Generating html format based on the 
    html_format = generate_network_report_html(data_list)

    ########################
    # Creating MIME object #
    ########################

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "ICMP Network Reachability Report"

    # Attaching the HTML content to the MIME object
    # The first argument is the content, the second is the content type ('html')
    msg.attach(MIMEText(html_format, 'html'))

    # Connecting to the SMTP server without authentication
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        server.quit()

    exit()
