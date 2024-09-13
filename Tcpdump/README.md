# Tcpdump - Capture your first packet 

## Scenario 
As a network analust, you are given a task who needs to use tcpdump to capture and analyze live network traffic from a Linux virtual machine.

Your Linux user's home directory contains a sample packet capture file that you will use at the end of the lab to answer a few questions about the network traffic that it contains.

## Solutions
### TASK 1. Identify Network Interfaces.
   
* Use `ifconfig` to identify the interfaces that are available:

![image](https://github.com/user-attachments/assets/bd4ad343-a400-4513-b6fa-8c91e2dc806d)

* Identify the interface options available for packet capture:

![image](https://github.com/user-attachments/assets/d5234266-711a-44b3-a45f-ee8f31e8a8a0)


### TASK 2. Inspect the network traffic of a network interface with tcpdump.

* Use `sudo tcpdump -i eth0 -v -c5` to filter live network packet data:
  
![image](https://github.com/user-attachments/assets/c7f87dc7-9e1b-4f2b-a2ae-8052e6360a0b)

> `-i eth0`: Capture data specifically drom the `eth0` interface.

> `-v`: Display detailed packet data.

> `-c5`: Capture 5 packets of data.


### TASK 3. Capture network traffic:

* Capture packet data into a file named called `capture.pcap`:  `sudo tcpdump -i eth0 -nn -c9 port 80 -w capture.pcap &`.

> `-i eth0`: Capture data from the eth0 interface.

> `-nn`: Do not attempt to resolve IP addresses or ports to names.This is best practice from a security perspective, as the lookup data may not be valid. It also prevents malicious actors from being alerted to an investigation.

> `-c9`: Capture 9 packets of data and then exit.

> `port 80`: Filter only port 80 traffic. This is the default HTTP port.

> `-w capture.pcap`: Save the captured data to the named file.

> `&`: This is an instruction to the Bash shell to run the command in the background.

![image](https://github.com/user-attachments/assets/db969ee8-e0f6-45f2-8019-c5ee5f149620)

* Use `curl` to generate some HTTP (port 80) traffic: `curl opensource.google.com`.
> Open a website and generate some HTTP (TCP Port 80) traffic that can be captured.   

![image](https://github.com/user-attachments/assets/696acbd7-bf7e-4bb0-bdd0-ca36f528a5d9)

* Verify the packet data has been captured: `ls -l capture.pcap`.

![image](https://github.com/user-attachments/assets/eb47422e-de5b-49d0-9ac9-fc2d7eae8f2b)


### TASK 4. Filter the captured packet data.
* Filter the packet header data from the `capture.pcap` capture file: `sudo tcpdump -nn -r capture.pcap -v`.

![image](https://github.com/user-attachments/assets/7cae7bb5-c8e6-4e91-9fc1-f1c2479ce55a)


![image](https://github.com/user-attachments/assets/4484a10c-de63-4165-a5bc-e68e409057c1)

> `-nn`: Disable port and protocol name lookup.

> `-r`: Read capture data from the named file.

> `-v`: Display detailed packet data. 

* Filter the extended packet data from the `capture.pcap` capture file: `sudo tcpdump -nn -r capture.pcap -X`.

![image](https://github.com/user-attachments/assets/ca4df3e0-c257-4012-aec9-4dcb7ff81e75)

![image](https://github.com/user-attachments/assets/a86b0aa5-1437-4366-a434-7952c4abf873)

![image](https://github.com/user-attachments/assets/f647b5cd-fa1f-4f99-93f2-ce632998edc5)

> `-nn`: Disable port and protocol name lookup.

> `-r`: Read capure data from the named file.

> `-X`: Display the hexadecimal and ASCII output format packet data. Security analysts can analyze hexadecimal and ASCII output to detect patterns or anomalies during malware analysis or forensic analysis.

> Note: Hexadecimal, also known as hex or base 16, uses 16 symbols to represent values, including the digits 0-9 and letters A, B, C, D, E, and F. American Standard Code for Information Interchange (ASCII) is a character encoding standard that uses a set of characters to represent text in digital form.






