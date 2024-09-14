# Intrusion Detection Systems (IDS) - Suricata
> Suricata is an open-source intrusion detection system, intrusion prevention system, and network analysis tool.

> An intrusion detection system (IDS) is an application that monitors system activity, alerts on possible intrusions and also to monitor the networks to identify indications of malicious activity.

## Step-by-step 

### Task 1: Examine a custom rule in Suricata

![image](https://github.com/user-attachments/assets/b5325d01-4d39-4e84-a908-064bcad601ee)

```
alert http $HOME_NET any -> $EXTERNAL_NET any (msg:"GET on wire"; flow:established,to_server; content:"GET"; http_method; sid:12345; rev:3;)
```

* Action
`Alert` : Instructs to alert on selected network traffic. The IDS will inspect the traffic packets and send out an alert in case it matches. 

* Header
`http`: The rule that applies is only to HTTP traffic. The arrow indicates the direction of the traffic from $HOME_NET and going to the destination IP address $EXTERNAL_NET. In this scenario, $HOME_NET is a suricata variable defined in `/etc/suricata/suricata/yaml` as a rule definitions.
$HOME_NET is definatd as the `172.21.224/0/20` subnet. 

* Rule options
`Rule`: Customize signatures with additional parameters.
  * The `msg`: The alert will print out the text `GET on wire`.
  * The `flow:established, to_server`: Determines that packet from the client to the server should be matched (The handshakes: SYN-ACK packet).
  * The `content`: "GET" tells Suricata to look for the word GET in the `http.method` of the packet.
  * The `sid:12345`: Unique numerical value that identify the rule.
  * The `rev:3` indicates the signature's version which is used to identify the signature's version.

    
### Task 2. Trigger a custom rule in Suricata

* List the files in the `/var/log/suricata` folder: `ls -l /var/log/suricata`. Up this task, there will be no files to be found.

![image](https://github.com/user-attachments/assets/15c5fe06-10bb-4a46-8985-7291d15b22ca)

* We run Suricata using the `custom.rules` and `sample.pcap`: `sudo suricata -r sample.pcap -S custom.rules -k none`.
  * The `-r sample.pcap` option specifies an input file to mimic network traffic. In this case, the sample.pcap file.
  * The `-S custom.rules` option instructs Suricata to use the rules defined in the custom.rules file.
  * The `-k none` option instructs Suricata to disable all checksum checks.

![image](https://github.com/user-attachments/assets/9c5a13bf-4086-406d-b678-e8ac6e77c049)

* List the files in the `/var/log/suricata` folder again: `ls -l /var/log/suricata`.

![image](https://github.com/user-attachments/assets/0be32c6e-a92d-4c85-8dbd-239d7ad3e95f)

* Display `fast.log`: `cat /var/log/suricata/fast.log`

![image](https://github.com/user-attachments/assets/66f6bd50-403d-46be-8c00-e3738ccd470f)


### Task 3. Examine eve.json output


















