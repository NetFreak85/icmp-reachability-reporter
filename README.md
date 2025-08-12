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

## 🚀 How to Use

1. Configuration
Create an ip_address.yaml file in the same directory as the script. This file will define the IP addresses to be tested and the ICMP parameters.

Here is an example of the ip_address.yaml file:

icmp:
    count: 5
    timeout: 2
    ttl: 100
    delay_inter_packages: 1
    verbose: False

ip_address:
    - ip: "8.8.8.8"
      description: "Google DNS Public Service"
    - ip: "151.101.0.81"
      description: "UK BBC News"
    - ip: "34.147.120.111"
      desription: "Spanish Sport News"

icmp: Contains global settings for the ping tests.

num_icmp_packages: The number of ICMP packets to send to each IP.

ttl: The Time-to-Live for the packets.

delay_inter_packages: The delay in seconds between sending packets to a single host.

ip_address: A list of dictionaries, where each dictionary specifies an IP and a description.
