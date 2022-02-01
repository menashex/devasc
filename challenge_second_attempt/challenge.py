import json
import requests

############## filter by Postal Codes starts with T1, T2, T3, or T4 and Advanced = False #################
lst=[]
with open("C:\\Users\\Menash\\Desktop\\challenge\\ham-db.json") as file:
    data = json.load(file)
    for i in data:
        if(i["postal"][0] == "T"):
            if(i["postal"][1] == "1" or i["postal"][1] == "2" or i["postal"][1] == "3" or i["postal"][1] == "4"):
                if(i["creds"]["advanced"] == False):
                    lst.append(i)
                else:
                    continue
            else:
                continue
        else:
            continue

############## send api request ################

url = "http://www.mapquestapi.com/directions/v2/routematrix"
headers = {}
params = {"key":"fOZH9aUyqvfeqYUTrq6hp4wOyG6R2HCB"}


counter=0
lst1=[]
with open("C:\\Users\\Menash\\Desktop\\challenge\\list.json","w") as file:
    for i in lst:
        body = {
            "locations": [
                "T3G 6A7",
                i["postal"]
            ]
        }
        response = requests.post(url=url,params=params,headers=headers, data=json.dumps(body)).json()
        if(response["distance"][1] < 45.0):
            lst1.append(i)
            data = json.dumps(i)
            file.write(data)
            file.write("\n")
            print(response["distance"][1],i)