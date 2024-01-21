import_file = "data/login.txt"
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"
with open(import_file, "a") as file: 
    file.write (missing_entry)
with open (import_file, "r")as file: 
    text = file.read ()
print (text.split())

import_file = "data/allow_list.txt"
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

with open (import_file, "w") as file: 
    file.write(ip_addresses)

with open (import_file, "r") as file: 
    text = file.read()

print (text)


#For this script to run it will need a place to import the file/data from 
