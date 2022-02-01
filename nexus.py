import json
import requests

username = "admin"
password = "Cisco123"

url = "https://10.10.20.58/ins"
headers = {
	'content-type' : 'application/json'
	}

payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show cdp nei",
    "output_format": "json"
  }
}

response = requests.post(url=url, data=json.dumps(payload),headers=headers,auth=(username,password),verify=False).json()
print(response)

auth_url = 'https://10.10.20.58/api/mo/aaaLogin.json'
auth_body = {"aaaUser": {"attributes": {"name":username,"pwd":password}}}

auth_response = requests.post(auth_url,data=json.dumps(auth_body),verify=False).json()
print(auth_response)
token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']
print("\n\n" ,token)
cookies={}
cookies['APIC-cookie']=token

counter = 33
while(counter <= 35):
	new_url = "https://10.10.20.58/api/node/mo/sys/intf/phys-[eth1/" + str(counter) +"].json"
	body={
	#'imdata':{
	    'l1PhysIf':{
	        'attributes':{
	            'adminSt':'up'}}}
	        

	response = requests.get(url = new_url, headers=headers, auth=(username,password),cookies=cookies,verify=False).json()
	print("configuring eth1/",counter,"        ",response)
	response = requests.post(url = new_url, data=json.dumps(body), headers=headers, auth=(username,password),cookies=cookies,verify=False).json()
	response = requests.get(url = new_url, headers=headers, auth=(username,password),cookies=cookies,verify=False).json()
	print(response)
	counter+=1