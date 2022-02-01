import requests
import json

url = "https://api.meraki.com/api/v0/organizations"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': 'cb083370ae1d1b4900db52145fe66239f4868df3'
}

response = requests.get(url, headers=headers, data=payload).json()


for i in response:
    if(i["name"] == "IPA"):
        nameid = i["id"]
        print(nameid, i["name"])

url = url +  "/" + nameid+ "/networks" 

response = requests.get(url, headers=headers, data=payload).json()

for i in response:
    if(i["name"] == "test_net - switch"):
        netid = i["id"]
        print(i["name"], netid)


