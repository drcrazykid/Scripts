import requests, json, tkinter as tk


# This free non-api token url recovers IP GeoLocation information.
url = "http://ip-api.com/json/"


# This url submits a IP request and delivers IP information. 
url2 = "https://api.ipify.org/?format=json"

response = requests.get(url2)
r = requests.get(url)



ip_info = dict()
label_list = []
stat_list = list()

root = tk.Tk()

root.title("My IP Information")
root.geometry("400x350")

for k,v in r.json().items():

    label = tk.Label(master=root, text=f"{k.capitalize()}: {v}")
    label_list.append(label)

for x in label_list:
    x.grid(row=label_list.index(x),column=0,sticky="w")

root.mainloop()