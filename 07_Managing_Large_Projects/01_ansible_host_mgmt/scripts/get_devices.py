import requests

base_url = "https://demo.netbox.dev/api/dcim/devices/"

payload={}
headers = {
  'Authorization': 'Token c02a90d9ba4dbc6bd05d628e8064e24289996e78'
}

response = requests.request("GET", base_url, headers=headers, data=payload)

#print(type(response.json()))
#print(response.json()["results"])

device_list = response.json()["results"]

def get_id(result):
    return result["id"]

device_ids = list(map(get_id, device_list))
print(device_ids)

def getDeviceDetails(device_id):
    device_url = base_url + str(device_id)
    device_response = requests.request("GET", device_url, headers=headers, data=payload)
    device_json = device_response.json()
    device_details = {}
    if(device_json["name"]):
        device_details["hostname"] = device_json["name"]
    elif (device_json["device_type"]):
        device_details["hostname"] = device_json["device_type"]["slug"]
    if(device_json["primary_ip4"]):
        device_details["ipaddress"] = device_json["primary_ip4"]["address"].split("/")[0]
    print(device_details)

device_id = input("Enter device id: ")
getDeviceDetails(device_id)