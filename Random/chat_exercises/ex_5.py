'''
LEVEL 3 — Multiprocessing Fundamentals

Exercise 5: Parallel Squaring (Multiprocessing) Goal: Square numbers
1–10 using multiple processes.

Concepts: - multiprocessing.Process - Queue - main guard

Constraints: - One process per number - Results collected in order

Hint: Put (n, n*n) into a queue.
'''
import os
from multiprocessing import Process, Queue

q = Queue()
sol = None

'''
big note is child processes can't read from nested functions and only some @staticmethods from
classes
'''
def square_worker(num:int,que:Queue):
    que.put(f"({num},{num*num})")
    # print(__name__)
    # print(f"({num},{num*num})")
if __name__ == "__main__":
    
    procs = []
    for x in range(10):
        p = Process(target=square_worker,args=(x,q),name=f"proc: {x}")
        p.start()
        print(f"Started: {p.name}")
        procs.append(p)
    
    for p in procs:
        p.join()
    for n in range(10):        
        sol = q.get()
        print(sol)
        