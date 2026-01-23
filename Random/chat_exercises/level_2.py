'''
LEVEL 2 — Scheduling & Control

Exercise 3: Periodic Worker (Threading + Event) Goal: Create a worker
thread that runs every 5 seconds and stops cleanly when signaled.

Concepts: - threading.Event - Graceful shutdown

Constraints: - No while True without sleep - Must stop within 1 second
of signal

Hint: Use event.wait(timeout) instead of time.sleep().
'''
from threading import Thread, Event
import os

def ex_3():
    stop_event = Event()

    def worker(interval:float):
        print("Worker started")
        
        while not stop_event.is_set():
            print("The worker is working...")

            stop_event.wait(interval)
                
        print("Recieved close command, shutting down gracefully")
            
    t = Thread(target=worker,args=(5,))
    
    t.start()
    
    try:
        input("Press ENTER to stop the worker...\n")
    finally:
        stop_event.set()
        t.join()
        print("Main thread exiting cleanly")
    


def ex_4():
    pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()

    response = input("Which exercise would you like to run? (3 or 4)\n")

    if response == "3":
        ex_3()
    elif response == "4":
        ex_4()
    else:
        print("Improper response, exiting...")

if __name__ == "__main__":
    main()