"""
1. Reading the file
2. extract ip address and error and success logs
3. save the output in csv/excel file
4. send email
"""
import re
import pandas as pd
import pprint

logfile = open("serverlogs.log", "r")

pattern = r"((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

ip_address_list = []
failed_list = []
success_list = []
for log in logfile:
    ip_add = re.search(pattern, log)
    ip_address_list.append(ip_add.group())
    list = log.split(" ")
    failed_list.append(int(list[-1]))
    success_list.append(int(list[-4]))

total_failed = sum(failed_list)
total_success = sum(success_list)
ip_address_list.append('Total')
success_list.append(total_success)
failed_list.append(total_failed)
df = pd.DataFrame(columns=['IP Address', 'Success', 'Failed'])
df['IP Address'] = ip_address_list
df['Success'] = success_list
df['Failed'] = failed_list

df.to_csv('output.csv', index = False)

pprint.pprint(df)
#print(ip_address_list)