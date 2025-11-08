import tkinter as tk
import time, psutil, subprocess, os


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
    font= ("Helevica", 14, "bold"),
    bg = "black",
    fg = "white"
)

cpu_label.grid(column=upper_right[0],row=upper_right[1])
cpu_label.configure(text="78")
# root.grid_columnconfigure(0,weight=1)
# root.grid_rowconfigure(0,weight=1)

for x in range(3):
    if x == 0:
        root.grid_columnconfigure(1,weight=1)
        root.grid_rowconfigure(x,weight=1)
    else:
        root.grid_rowconfigure(x,weight=1)
    print(x)

def get_cpu_temp(return_as_string=True):
    if os.name == "nt":
        pass
        
    else:
        print(psutil.sensors_temperatures())
        print(t)
    # place in logic for retrieving cpu temp
    cpu_temp = 104
    if return_as_string:
        return str(cpu_temp)
    else:
        return cpu_temp

def update_display():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %B %d, %Y")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    
    cpu_label.config(text=get_cpu_temp())

    root.after(1000, update_display)
    
def quit_fullscreen(event):
    root.attributes('-fullscreen',False)
    root.destroy()

root.bind("<Escape>", quit_fullscreen)

update_display()
root.mainloop()