import requests, json


# This free non-api token url recovers IP GeoLocation information.
url = "http://ip-api.com/json/"


# This url submits a IP request and delivers IP information. 
url2 = "https://api.ipify.org/?format=json"

response = requests.get(url2)

print(response.json())