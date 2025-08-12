IP Address Configuration and Validation

This project provides a simple configuration file and Python script for working with IP addresses, including ICMP ping settings and IP address validation.

Table of Contents





Overview



Files



Configuration



Usage



Dependencies



License

Overview

The project includes a YAML configuration file (ip_address.yaml) that defines ICMP ping settings and a list of IP addresses with their descriptions. Additionally, a Python script (my_ipaddress.py) demonstrates basic IP address validation using the ipaddress module.

Files





ip_address.yaml: Configuration file containing ICMP settings and a list of IP addresses with descriptions.



my_ipaddress.py: Python script to validate if a given IP address is private.

Configuration

The ip_address.yaml file contains the following settings:

ICMP Settings





count: Number of ICMP packets to send (default: 5)



timeout: Timeout for each ICMP request in seconds (default: 2)



ttl: Time-to-live for ICMP packets (default: 100)



delay_inter_packages: Delay between ICMP packets in seconds (default: 1)



verbose: Enable verbose output (default: False)

IP Addresses

The file lists IP addresses with their descriptions:





8.8.8.8: Google DNS Public Service



151.101.0.81: UK BBC News



34.147.120.111: Spanish Sport News

Note: There is a typo in the YAML file (desription instead of description) for the Spanish Sport News entry. Consider correcting this for consistency.

Usage





Configuration:





Edit ip_address.yaml to modify ICMP settings or add/remove IP addresses as needed.



IP Address Validation:





Run the my_ipaddress.py script to check if an IP address is private:

python my_ipaddress.py



The script currently checks the IP address 197.23.4.11 and prints whether it is private.



Extending the Script:





You can modify my_ipaddress.py to read IPs from ip_address.yaml and perform actions like pinging or further validation. For example, you could use the ping3 library to ping the IPs listed in the YAML file based on the ICMP settings.

Dependencies





Python 3.x



ipaddress module (included in Python standard library)



(Optional) pyyaml for reading the YAML configuration if you extend the script:

pip install pyyaml

License

This project is licensed under the MIT License. See the LICENSE file for details.
