# Network Test

This project automates the monitoring of network devices within the same IP range.
The script reads a list of devices, checks their online/offline status using ping or TCP,
and generates a formatted report in a text file.


## Features
- Reads devices from a text file (`cam.txt`)
- Checks device status using ICMP ping or TCP connection
- Generates a clean, formatted report (`report.txt`)
- Modular design with separate files for reading, pinging, and reporting


## Usage
1. Add devices to `cam.txt` in the format:


Name | Model | IP

2. Run the main script:
```bash
python main.py

3.Check report.txt for the results.

Name: cam01
Model: type01
IP: 192.168.xxx.xxx
Status: Online
-------------
Name: cam02
Model: type 02
IP: 192.168.xxx
Status: Offline
-------------


Notes
Only devices in the same IP range are checked.
