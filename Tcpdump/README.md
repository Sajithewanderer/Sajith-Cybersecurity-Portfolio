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

