import urllib, json

url = "http://10.102.62.236:3000/users/userlist"

response = urllib.urlopen(url)
data = json.loads(response.read())

# removing the user information by taking it's email-id as input

def db_search(a):
	email = raw_input("Enter the email id of user:\n")
	
	index = -1
	for i in range(len(a)):
		if a[i]['email']==email: 
			index = i
			break
	if index == -1:
		print "Not found"	

	a.remove(a[index])

print "Old database: ",data

db_search(data)

print "New database: ",data

