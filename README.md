# 📡 ICMP Reachability Checker

This Python script performs ICMP (Internet Control Message Protocol) reachability tests on a list of IP addresses. It's designed to concurrently ping multiple devices, collect statistics, and generate an HTML report that's sent via email.

The script uses `scapy` for packet manipulation and `concurrent.futures` for efficient, multi-threaded execution.

## 📝 Features

* **Concurrent Pinging**: Tests multiple IP addresses at the same time using threading.
* **YAML Configuration**: Easily configure IP addresses, descriptions, and ICMP parameters in a `ip_address.yaml` file.
* **Detailed Statistics**: Collects and reports on RTT (Round Trip Time) statistics (min, max, avg) and packet loss.
* **HTML Reporting**: Generates a clean, human-readable HTML report summarizing the results.
* **Email Notifications**: Sends the HTML report as an email using an SMTP server.

## ⚙️ Prerequisites

To run this script, you need to have the following Python libraries installed:

* **`scapy`**: For sending and receiving network packets.
* **`PyYAML`**: To parse the configuration file.

You can install these packages using `pip`:

```bash
pip install scapy pyyaml
```

## Setup

1.  **Clone the Repository**:
```bash
    git clone https://github.com/NetFreak85/icmp-reachability-reporter.git
    cd icmp-reachability-reporter
```
2. Configure ip_reachibility.py Script for Email.
```bash
    sender_email: The email address from which the report will be sent.
    receiver_email: The email address to which the report will be sent.
    smtp_server: The address of your SMTP server.
    smtp_port: The port for your SMTP server (e.g., 25 for unencrypted, 587 for TLS/STARTTLS, 465 for SSL).
```
Email Var Config Section in ip_reachibility.py:
```python
    # Sender Email Address
    sender_email = "inpro.base@bbva.com"

    # Receiver Email Address
    receiver_email = "joserafael.guerra.tech@bbva.com"

    # SMTP Server Address
    smtp_server = "smtp.es.nextgen.igrupobbva"

    # SMTP Port
    smtp_port = 25
```

Note: This script is configured to use an unauthenticated SMTP server. If your server requires authentication, you will need to modify the smtplib.SMTP() call and add server.login() with your credentials.

3. Running the Script

Execute the script from your terminal:

```bash
    python ip_reachibility.py
```

    The script will:

* **Read the IP addresses and parameters from ip_address.yaml.
* **Ping each IP address concurrently.
* **Collect all the results.
* **Generate a detailed HTML report.
* **Send the report to the configured email address.
* **Exit.

## ⚙️ Code Details

```ping_ip(ip_info, icmp_params)```
This function handles the core ICMP pinging logic for a single IP address. It sends a specified number of packets, measures the RTT for each successful reply, and calculates the minimum, maximum, and average RTT. It returns a dictionary containing all the statistics.

```ICMP_reachibility()```
This is the main function that orchestrates the concurrent execution. It reads the YAML configuration, creates a ThreadPoolExecutor, and submits a ping_ip task for each IP address. It then gathers the results from all the threads and returns a list of result dictionaries.

```generate_network_report_html(data)```
This function takes the list of results and dynamically generates a single HTML string. It iterates through the data for each IP, formats the statistics, and creates a visually appealing report with status badges (Reachable, Partial Loss, Unreachable) based on the packet loss percentage.

```Main Program (if name == 'main':)```
The main execution block calls ICMP_reachibility() to get the data, passes the data to generate_network_report_html() to create the report, and finally uses smtplib to connect to the SMTP server and send the email with the attached HTML report.
