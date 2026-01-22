'''
Level 1:
Exercise 1: Background Countdown (Threading)

🎯 Goal
Run a countdown timer in the background while the main program prints dots every second.

🧠 Teaches

threading.Thread

Daemon threads

Non-blocking execution

🧩 Constraints

Countdown sleeps 1 second between numbers

Main loop prints "." every second

Program exits cleanly after countdown finishes

🏁 Hint
Use daemon=True and a shared variable or join() (CLI only)'''

def ex_1():
    from threading import Thread
    from time import sleep

    def worker_print(start: int):
        for i in range(start, -1, -1):
            print(num)        
            sleep(1)
        

    num = 5

    task = Thread(target=worker_print, args=(num,), daemon=True)
    task.start()

    while task.is_alive():
    
        print(".")
        sleep(1)


'''
Exercise 2: API Fetcher (Threading + Queue) Goal: Fetch data from 3 URLs
concurrently and print results as they arrive.

Concepts: - Thread safety - Queue - Avoiding shared state

Constraints: - Use requests - One thread per URL - Main thread prints
results

Hint: Each worker puts (url, status_code) into a queue.
'''
def ex_2():
    from queue import Queue
    from threading import Thread
    import requests

    q = Queue()
    cached_url_info = None
    
    def url_fetcher(url:str):
        nonlocal q
        try:
            r = requests.get(url=url)
            r.raise_for_status()
            q.put({"url":url,"status":r.status_code})
        except Exception as e:
            q.put({"url":str(e)})
    
    url_list = ["https://www.google.com","https://www.facebook.com","https://www.msn.com"]

    threads = []    
    for u in url_list:
        t = Thread(target=url_fetcher, args=(u,),daemon=True)
        t.start()
        threads.append(t)
    
    for _ in range(len(url_list)):

        cached_url_info = q.get()
        print(cached_url_info)

    

ex_2()