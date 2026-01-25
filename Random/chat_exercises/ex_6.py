'''
Exercise 6: CPU Stress Test Goal: Compute prime numbers up to 200,000
using: 1) Single process 2) Multiple processes

Concepts: - GIL impact - Performance comparison

Constraints: - Time both versions - Use time.perf_counter()

Hint: Split the range into chunks per process.
'''
from multiprocessing import Process,Queue
from primebenchmark import PrimeBenchmark
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def compute_primes(start:int, end:int,queue:Queue=None):
    primes = []

    for x in range(start,end):
        if is_prime(x):
            primes.append(x)
    if not None:
        queue.put(primes)

def main():
    que = Queue()
    holder = None
    pb = PrimeBenchmark(0,200_001)
    
    single_time, primes = pb.run_single()
    
    print(f"Single Process Total time: {single_time} seconds")

    # Multiprocessing way

    procs = []
    chunks = [(0,50_000),(50_000,100_000),(100_000,150_000),(150_000,200_001)]

    start = time.perf_counter()

    for x in range(4):
        p = Process(target=compute_primes,args=(chunks[x][0],chunks[x][1],que))
        p.start()
        procs.append(p)


    final_primes = []
    for p in procs:
        holder = que.get()
        
        for x in holder:
            final_primes.append(x)    
    
    for p in procs:
        p.join()
    stop = time.perf_counter()

    multi_time = round(stop-start,5)
    print(f"Multi-Process Total time: {multi_time} seconds")

    print(f"Using multiple processor is {round(single_time / multi_time,2)} times faster")

    print(len(final_primes))
    
if __name__ == "__main__":
    main()