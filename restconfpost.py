import requests

url = "https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces"

payload="{\r\n    \"ietf-interfaces:interface\": {\r\n        \"name\":\"Loopback109\",\r\n        \"description\":\"added by menash\",\r\n        \"type\":\"iana-if-type:softwareLoopback\",\r\n        \"enabled\":true,\r\n        \"ietf-ip:ipv4\":{\r\n            \"address\":{\r\n                \"ip\":\"10.10.10.10\",\r\n                \"netmask\": \"255.255.255.0\"\r\n            }\r\n        }\r\n    }\r\n}"
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
