import requests
import json

url = "http://35.172.223.190:5000/ThermsAreUs/api/v1.0/current-setpoint"
response = requests.get(url)
s = response.json()
setpoint = s['current_setpoint']
print("The current room setpoint is " + str(setpoint) + " degrees.")
headers = {'Content-Type': "application/json", 'Accept': "application/json"}
data={'newsetpt': 90}
r = requests.put(url, json=data, headers=headers)
print(r)
