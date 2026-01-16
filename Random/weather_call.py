import requests, os, json
from time import sleep
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")
zip = "78253"
url = f"http://api.weatherapi.com/v1/current.json"

parameters = {
    "key":KEY,
    "q":zip
}
r = requests.get(url=url,params=parameters)

data = r.json()
print(data)
# with open("san_antonio.json", "w") as f:
#     json.dump(data,f, indent=4)

# for x in range(10):
#     r = requests.get(url=url)

#     data = r.json()

#     print(f"City: {data['location']['name']} Temperature: {data["current"]["temp_f"]}\tAs of: {data["current"]["last_updated"]}")
#     sleep(5)
#     x+=1
