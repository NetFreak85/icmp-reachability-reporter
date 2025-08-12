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

