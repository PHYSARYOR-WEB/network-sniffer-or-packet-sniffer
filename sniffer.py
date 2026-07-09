# Network Packet Sniffer

A lightweight, Python-based network packet sniffer that captures and analyzes live network traffic in real-time. This tool processes packets at the network layer to extract key details such as source/destination IP addresses, protocols, and raw payload data.

## 🚀 Features
* **Real-Time Capture:** Sniffs active network traffic passing through your network interface.
* **Protocol Identification:** Parses network layers to identify protocols (like UDP and TCP).
* **IP Tracking:** Dissects packets to display clear Source and Destination IP addresses.
* **Payload Inspection:** Extracts and prints a raw snippet of the packet's payload data for deep-dive analysis.

## 🛠️ Prerequisites & Installation

This tool utilizes **Scapy**, a powerful interactive packet manipulation library for Python.

1. Ensure you are using a Linux environment and have Python 3 installed.
2. Install the required dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-scapy -y
