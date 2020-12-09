import json
import requests
requests.packages.urllib3.disable_warnings()
 
api_url = "https://10.215.26.173/restconf/data/ietf-interfaces:interfaces/interface=Loopback13"
 
headers = { "Accept": "application/yang-data+json",
            "Content-type":"application/yang-data+json"
           }
basicauth = ("admin", "vnpro@149")
 
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback13",
        "description": "[Student\'s Name] loopback interface",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.1.23.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
 
 
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
 
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code, resp.json()))
