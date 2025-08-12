# ICMP Reachability Checker

This Python script, `ip_reachibility.py`, checks the ICMP reachability of multiple IP addresses concurrently using threading. It reads a list of IP addresses from a YAML configuration file, performs a series of ICMP pings to each, and then generates and emails an HTML report of the results.

## Features

- **Concurrent Execution**: Uses `concurrent.futures.ThreadPoolExecutor` for simultaneous ICMP pings to multiple IP addresses, improving performance.
- **Configurable**: Ping parameters like packet count, timeout, and delay are customizable in the `ip_address.yaml` file.
- **YAML Configuration**: IP addresses and their descriptions are stored in `ip_address.yaml`, making it easy to add or remove devices.
- **HTML Report Generation**: Creates a detailed HTML report with RTT (Round-Trip Time) statistics (min, max, avg) and packet loss percentage for each IP address.
- **Email Notifications**: Automatically sends the generated HTML report via email to a configured recipient.

## Prerequisites

- **Python 3.x**: The script is written in Python 3.
- **Required Python Libraries**:
  - `PyYAML`: For parsing the YAML configuration file.
  - `scapy`: For sending and receiving ICMP packets.

You can install these libraries using pip:

```bash
pip install pyyaml scapy

