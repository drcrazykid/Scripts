import tkinter as tk
import time, psutil, threading, os, requests
from dotenv import load_dotenv
from queue import Queue
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
    
    weather_queue = Queue()
    cached_weather = None
    
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
    
    def fetch_weather():
        KEY = os.getenv("KEY")
        zipcode = "78253"
        url = "http://api.weatherapi.com/v1/current.json"
        params = {
            ""
            "key":KEY,
            "q":zipcode,
            "aqi": "no"
            }
        try:
            resp = requests.get(url=url,params=params, timeout=10)
            resp.raise_for_status()
            weather_queue.put(resp.json())
        except Exception as e:
            weather_queue.put({"error": str(e)})

    def schedule_weather_update():
        threading.Thread(target=fetch_weather, daemon=True).start()
        root.after(15 * 60 * 1000, schedule_weather_update)        

        
    def update_display():
        nonlocal cached_weather

        # Pulls new weather if available
        while not weather_queue.empty():
            cached_weather = weather_queue.get()

        if cached_weather:
            if "error" in cached_weather:
                pass
            else:
                info = cached_weather
                city = info["location"]['name']
                state = info["location"]["region"]
                temp = info["current"]["temp_f"]
                last = info["current"]['last_updated']

                weather_string = f"{city}, {state}: {temp}°F"
                last = f"Last Updated: {last}"

                temp_label.config(text=weather_string)
                last_label.config(text=last)
                
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%A, %B %d, %Y")
        
        clock_label.config(text=current_time)
        date_label.config(text=current_date)
        cpu_label.config(text=f"CPU: {get_cpu_temp()}")

        
        root.after(1000, update_display)
        
    def quit_fullscreen(event):
        root.attributes('-fullscreen',False)
        root.destroy()

    root.bind("<Escape>", quit_fullscreen)
    update_display()
    schedule_weather_update()
    root.mainloop()

if __name__ == "__main__":
    main()