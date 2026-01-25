'''
Exercise 6: CPU Stress Test Goal: Compute prime numbers up to 200,000
using: 1) Single process 2) Multiple processes

Concepts: - GIL impact - Performance comparison

Constraints: - Time both versions - Use time.perf_counter()

Hint: Split the range into chunks per process.
'''
from multiprocessing import Process,Queue
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def compute_primes(start:int, end:int,queue:Queue,chunk_size=1,multiprocess=False):
    primes = []

    if not multiprocess:
        
        for x in range(start,end):
            if is_prime(x):
                primes.append(x)
        
        queue.put(primes)
    else:    
        pass
def main():
    que = Queue()
    holder = None
    start = time.perf_counter()

    compute_primes(0,200_000,que)

    stop = time.perf_counter()
    single_time = round(stop-start,5)
    print(f"Single Process Total time: {single_time} seconds")

    # Multiprocessing way

    procs = []
    chunks = [(0,49_999),(50_000,99_999),(100_000,149_999),(150_000,200_000)]

    start = time.perf_counter()

    for x in range(4):
        p = Process(target=compute_primes,args=(chunks[x][0],chunks[x][1],que))
        p.start()
        procs.append(p)


    final_primes = []
    for p in procs:
        if not que.empty():
            holder = que.get()
        
        for x in holder:
            final_primes.append(x)    
        p.join()
    stop = time.perf_counter()

    multi_time = round(stop-start,5)
    print(f"Multi-Process Total time: {multi_time} seconds")

    print(f"Using multiple processor is {round(single_time / multi_time,2)} times faster")

    print(len(final_primes))
    
if __name__ == "__main__":
    main()