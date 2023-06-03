import json

a = open("data.txt", "r")
b = json.load(a)
first_name = sorted([value for i in b for key, value in i.items() if key == "first_name"])
last_name = sorted([value for i in b for key, value in i.items() if key == "last_name"])
email = sorted([value for i in b for key, value in i.items() if key == "email"])
ip_address1 = sorted([value for i in b for key, value in i.items() if key == "ip_address"])

first_name_file = open("first_name.txt", "w")
first_name_file.write(str(first_name))
last_name_file = open("last_name.txt", "w")
last_name_file.write(str(last_name))
email_file = open("email.txt", "w")
email_file.write(str(email))
ip_address_file = open("ip_address.txt", "w")
ip_address_file.write(str(ip_address1))