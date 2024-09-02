# Network Traffic Monitoring and Attack Detection using Wireshark

## Objective: 
### -A small-size enterprise wants to detect and inspect certain TCP/IP network traffic on their server; specifically web traffic.
### -Lets set up and demonstrate Wireshark's packet capture capabilities.

## Tasks:
### 1.	Using Wireshark to capture packets on an ethernet port and save the capture data to a file.
 (->Start packet capture ->stop capture->save the packets to a file and load the capture file [8.8.8.8 is a DNS server for Google.com])
 ![image](https://github.com/user-attachments/assets/3cff9f10-65c0-49e5-94ec-1ae94fe1c1ad)
 ![image](https://github.com/user-attachments/assets/9897fec7-a90b-4cf8-bb59-29cf1beae95d)
 ![image](https://github.com/user-attachments/assets/6dabc9d5-70fa-44f2-bf07-6f0d7fbf18b3)

### 2.	Use the display filter to detect HTTP packets.
(Visiting http://cygwin.com to capture the HTTP packets. tcp.port==80)
![image](https://github.com/user-attachments/assets/22172ed8-6155-4a17-845d-76f6674c9cf2)
![image](https://github.com/user-attachments/assets/c9c35419-83d1-4cbb-9ddd-e4c4360afd59)

### 3.	Visit a web page and detect its IP address using a display filter. HTTPS tcp.port = 443
(filtering https packets by tcp.port==443 using a display filter)
![image](https://github.com/user-attachments/assets/7b928f58-9fb8-41a4-a9de-231bf9013738)
![image](https://github.com/user-attachments/assets/166a1cfa-1dd5-491d-9269-245919e3ddc1)

(TLS handshake display filter || tls.handshake.type==1)
![image](https://github.com/user-attachments/assets/a230a2a9-b0e8-4b0c-88b3-c8871af61976)

### 4.	Locate all HTTPS packets from a capture not containing a certain IP address. 
[ !(ip.addr == 142.250.67.46) and (tcp.port==443) ]
![image](https://github.com/user-attachments/assets/6e1afa40-9516-4317-a16e-81ed9f271722)


### 5.	Locate all the HTTPS and HTTP packets from a capture not containing a certain IP address.
[!(ip.addr == 142.250.67.46) and (tcp.port==443 or tcp.port==80)]
![image](https://github.com/user-attachments/assets/0d2b632e-93f3-4ab0-959d-c6bbcf1d3232)






