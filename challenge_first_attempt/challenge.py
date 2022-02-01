#!/usr/bin/env python3

import json
import requests

def getloc(location):
        return '{\"locations\":[\"T3B 0H8\",' + location + ']}'

def location(loc):
        if (loc['postal'].split(" ",)[0]).startswith("T1") and (loc.get("creds").get("advanced")==False):
                return True
        if (loc['postal'].split(" ",)[0]).startswith("T2") and (loc.get("creds").get("advanced")==False):
                return True
        if (loc['postal'].split(" ",)[0]).startswith("T3") and (loc.get("creds").get("advanced")==False):
                return True
        if (loc['postal'].split(" ",)[0]).startswith("T4") and (loc.get("creds").get("advanced")==False):
                return True
        return False



close=[]
close2=[]
with open("C:\\Users\\Menash\\Desktop\\challenge\\ham-db.json") as file:
        data = json.load(file)
        for i in data:
                if(location(i)):
                        close.append(i)

url = "http://www.mapquestapi.com/directions/v2/routematrix?key=kfceXAUxXdF2sHQZWJ6dfeerI2UHLq2A&inFormat=json&outFormat=json"
for i in close:
    body =  getloc(i.get("postal"))
    request1=requests.get(url, data=body)
    jsonreply=json.loads(request1.text)
    if((float(jsonreply.get("distance")[1])) < 45.0):
        close2.append(i)
        print(i, float(jsonreply.get("distance")[1]))
print(close2)
