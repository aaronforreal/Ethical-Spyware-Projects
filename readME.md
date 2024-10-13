# Simple Port Scanner

This is a simple Python-based port scanning tool that attempts to connect to a specified range of ports on a given target (IP address or hostname). It uses socket programming to check if the ports are open.

## Features
- Scans ports in the range 50 to 85 (by default, can be modified).
- Outputs the time the scan started and lists open ports.
- Handles errors such as host resolution failure and connection issues.
- Provides a simple command-line interface.

## Prerequisites

Make sure you have Python 3.x installed. You can check your version by running:

```bash
python3 --version

Installation

    Clone the repository or download the Python script.
    Open a terminal and navigate to the folder where the script is located.

Usage

To run the port scanner, use the following command:

bash

python3 scanner.py <ip>

Where <ip> is the target IP address or hostname you wish to scan.
Example

bash

python3 scanner.py 192.168.1.1

This will scan ports from 50 to 85 on the IP 192.168.1.1 and display which ports are open.
Error Handling

    If the hostname cannot be resolved, you will see an error message: Hostname could not be resolved.
    If the connection to the target fails, the script will print: Could not connect to server.
    To exit the program prematurely, press Ctrl + C.

How it Works

    The script takes one argument (the target IP/hostname).
    It then scans a specified range of ports (default: 50-85) to check which are open.
    For each open port, it prints a message like: Port 80 is open.
    The script handles common errors like invalid IP addresses and network failures.

Future Enhancements

    Allow users to specify custom port ranges.
    Add more detailed reporting features.
    Implement multi-threading to speed up the scan.

License

This project is licensed under the MIT License - see the LICENSE file for details
