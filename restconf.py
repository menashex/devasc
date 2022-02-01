import requests

headers = {
"Accept": "application/yang-data+json",
"Content-Type": "application/yang-data+json",
"Authorization": "Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU=",
}


url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces"
reply = requests.request("GET",url=url, headers=headers)
print(reply.text)
with open("C:\\Users\\Menash\\Desktop\\ietf.txt","w") as file:
    file.write(reply.text)