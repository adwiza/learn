import json
import csv
import re

all_users_tpgu = ('AD/users-all.csv')
all_users_hq = ('AD/ad_hq.csv')

users_tpgu_list = set()
users_hq_list = set()
email_pattern = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'


with open(all_users_tpgu, 'r') as data_file:
    users_tpgu = csv.reader(data_file)
    for line in users_tpgu:
        matched = re.findall(email_pattern, line[0])
        users_tpgu_list.add(str(matched[0][0]).lower())

with open(all_users_hq, 'r', encoding='utf-16') as data_file:
    users_hq = csv.reader(data_file, delimiter=';')
    for row in users_hq:
        users_hq_list.add(row[6].lower())

wrong_logins = list(users_tpgu_list.difference(users_hq_list))

wrong_logins_list = []
for login in wrong_logins:
    wrong_logins_list.append([login])

print(wrong_logins_list)
fields = ['Username']


with open('wrong_logins.csv', 'w', newline='') as out_csv:
    writer = csv.writer(out_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(fields)
    writer.writerows(wrong_logins_list)
