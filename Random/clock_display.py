import tkinter as tk
import time, psutil, subprocess, os, requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    if os.name == 'nt':
        import wmi
        print("imported wmi successfully")


    # basic window configuration
    root = tk.Tk()
    root.title("Pi5 Clock")
    root.configure(bg="black")
    root.attributes('-fullscreen',True)

    clock_label = tk.Label(
        root,
        font = ("Helvetica",200, "bold"),
        bg="black",
        fg="cyan"
    )

    # positions on display
    upper_left = 0,0
    upper_mid = 1,0
    upper_right = 2,0

    mid_left = 0,1
    mid_mid = 1,1
    mid_right = 2,1

    low_left = 0,2
    low_mid = 1,2
    low_right = 2,2

    clock_label.grid(column=mid_mid[0],row=mid_mid[1], sticky="nsew")


    date_label = tk.Label(
        root,
        font = ("Helvetica", 60),
        bg = "black",
        fg = "white"
    )

    date_label.grid(column=low_mid[0],row=low_mid[1], sticky="nsew")


    cpu_label = tk.Label(
        root,
        font= ("Helevica", 16, "bold"),
        bg = "black",
        fg = "white"
    )

    cpu_label.grid(column=upper_right[0],row=upper_right[1])
    cpu_label.configure(text="78")
    # root.grid_columnconfigure(0,weight=1)
    # root.grid_rowconfigure(0,weight=1)

    temp_label = tk.Label(
        root,
        font = ("Helvetica", 18, "bold"),
        bg = "black",
        fg = "white"
    )
    temp_label.grid(column=upper_left[0],row=upper_left[1])
    last_label = tk.Label(
        root,
        font = ("Helvetica", 10, "bold"),
        bg = "black",
        fg = "white"
    )
    last_label.grid(column=low_left[0],row=low_left[1])

    for x in range(3):
        if x == 0:
            root.grid_columnconfigure(1,weight=1)
            root.grid_rowconfigure(x,weight=1)
        else:
            root.grid_rowconfigure(x,weight=1)
        print(x)

    def get_cpu_temp():
        if os.name == "nt":
            pass
            
        else:
            cpu_temp = psutil.sensors_temperatures()['cpu_thermal'][0].current
            # convert to F and round to tenths
            c = round((cpu_temp * 5/9) + 32, 1)
        return c
    
    def get_weather():
        KEY = os.getenv("KEY")
        zipcode = "78253"
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            ""
            "key":KEY,
            "q":zipcode,
            "aqi": "no"
            }
        resp = requests.get(url=url,params=params)
        print(f"Response Code: {resp.status_code}")
        info = resp.json()

        city = info["location"]['name']
        state = info["location"]["region"]
        temp = info["current"]["temp_f"]
        last = info["current"]['last_updated']

        weather_strings = []
        weather_string = f"{city}, {state}: {temp}°F"
        last = f"Last Updated: {last}"
        weather_strings.append(weather_string)
        weather_strings.append(last)

        return weather_strings
        
    def update_display():
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %B %d, %Y")
        
        clock_label.config(text=current_time)
        date_label.config(text=current_date)
        cpu_label.config(text=f"CPU: {get_cpu_temp()}")

        # temp_label.config(text=get_weather()[0])
        # last_label.config(text=get_weather()[1])
        root.after(1000, update_display)
        
    def quit_fullscreen(event):
        root.attributes('-fullscreen',False)
        root.destroy()

    root.bind("<Escape>", quit_fullscreen)
    get_weather()
    update_display()
    root.mainloop()

if __name__ == "__main__":
    main()