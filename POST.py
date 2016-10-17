import requests
import json

payload = {}
#create an empty dictionary
url = "http://10.102.62.236:3000/users/adduser"

#Insert the data in dictionary
payload['username'] = str(raw_input("Enter username : "))
payload['email'] = str(raw_input("Enter email : "))
payload['fullname'] = str(raw_input("Enter fullname : "))
payload['age'] = str(raw_input("Enter age : "))
payload['location'] = str(raw_input("Enter location : "))
payload['gender'] = str(raw_input("Enter gender: "))

r = requests.post(url, data=json.dumps(payload))

print(r.text)
