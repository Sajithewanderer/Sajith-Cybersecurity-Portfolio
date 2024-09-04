# TASK:
## You are a security professional working at a health care company. As part of your job, you're required to regularly update a file that identifies the employees who can access restricted content. The contents of the file are based on who is working with personal patient records. Employees are restricted access based on their IP address. There is an allow list for IP addresses permitted to sign into the restricted subnetwork. There's also a remove list that identifies which employees you must remove from this allow list.

## Your task is to create an algorithm that uses Python code to check whether the allow list contains any IP addresses identified on the remove list. If so, you should remove those IP addresses from the file containing the allow list.

# Reading the file contents:
![image](https://github.com/user-attachments/assets/831d3f2d-e407-4326-8bdb-4d4fd960fb1f)

## The allow_list.txt contains certain IP address in a String format.
ip_address
192.168.25.60
192.168.205.12
192.168.97.225
192.168.6.9
192.168.52.90
192.168.158.170
192.168.90.124
192.168.186.176
192.168.133.188
192.168.203.198
192.168.201.40
192.168.218.219
192.168.52.37
192.168.156.224
192.168.60.153
192.168.58.57
192.168.69.116

## Convert String into a List Using a split() method.
![image](https://github.com/user-attachments/assets/e3b332d2-56ce-45c2-8a09-4f3cc66c9fdb)

## Remove IP Addresses That Are on the Remove List.
![image](https://github.com/user-attachments/assets/92681a03-a7a7-4943-95cb-dd500839fc64)

## Update the File With the Revised List of IP Addresses.
![image](https://github.com/user-attachments/assets/8b952981-2bc4-496e-a9d1-65cd5c9a1fc3)

OUTPUT:
## All the restricted IP addresses has been removed from the "allow_list.txt"
![image](https://github.com/user-attachments/assets/b7fb2383-ea32-425c-ac1c-5967b8bbb69e)




