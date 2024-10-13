#!/bin/python3

# Import necessary modules
import sys        # for system-specific parameters and functions
import socket     # for creating network connections
from datetime import datetime  # for getting the current time

# defining target
if len(sys.argv) == 2:  # Check if exactly one argument is passed (the target IP/hostname)
    target = socket.gethostbyname(sys.argv[1])  # Translate the hostname into an IPv4 address
else:
    # If the argument is missing, print an error message and the correct syntax
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")
    
# Banner to indicate the start of scanning
print(f"-" * 50)
print(f"Scanning target: " + target)  # Show the target IP/hostname being scanned
print(f"Time started: " + str(datetime.now()))  # Print the current time when scanning starts
print(f"-" * 50)

try:
    # Scan ports in the range from 50 to 85
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new socket
        socket.setdefaulttimeout(1)  # Set a timeout of 1 second for each connection attempt
        result = s.connect_ex((target, port))  # Try to connect to the target on the specified port
        if result == 0:  # If the connection is successful (port is open), result will be 0
            print(f"Port {port} is open")  # Print that the port is open
        s.close()  # Close the socket after the check

except KeyboardInterrupt:
    # Handle the case where the user interrupts the program (Ctrl + C)
    print(f"\nExiting Program")
    sys.exit()  # Exit the program

except socket.gaierror:
    # Handle the case where the hostname cannot be resolved to an IP address
    print(f"Hostname could not be resolved")
    sys.exit()  # Exit the program

except socket.error:
    # Handle errors related to socket connections, such as not being able to connect to the server
    print(f"Could not connect to server")
    sys.exit()  # Exit the program
