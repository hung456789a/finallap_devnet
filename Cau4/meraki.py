import requests
import json
base_url = "https://api.meraki.com/api/v1"
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

def get_orgs():
    url = f"{base_url}/organizations"

    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }

    response = requests.get(url=url, headers=header,)
    data = response.json()
    # print(json.dumps(data, indent=4))
    return data 

def get_orgs_inv_devices():
    org_id = 681155
    url = f"{base_url}/organizations/{org_id}/inventory/devices"
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Cisco-Meraki-API-Key": api_key
    }    
    response = requests.get(url=url, headers=header,)
    i = response.json()
    print(json.dumps(i,indent=4))
    return i


def find_device():
    device = get_orgs_inv_devices()

    for i in range(len(device)):
        if device[i]["networkId"] == "None":
            print(device[i])

if __name__=="__main__":
    # get_orgs()
    # get_orgs_inv_devices()
    find_device()