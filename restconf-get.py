import json
import requests
requests.packages.urllib3.disable_warnings()
 
api_url = "https://10.215.26.173/restconf/data/ietf-interfaces:interfaces"
 
headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"}
 
basicauth = ("admin", "vnpro@149")
 
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
 
print(resp)
 
response_json = resp.json()
 
print(json.dumps(response_json, indent=4))
