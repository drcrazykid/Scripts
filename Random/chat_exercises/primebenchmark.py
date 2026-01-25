import time
from multiprocessing import Queue

class PrimeBenchmark:
    def __init__(self, start:int, end:int, workers: int = 4):
        self.start = start
        self.end = end
        self.workers = workers
    
    @staticmethod
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def compute_chunk(start, end, queue):
        local_primes = []

        for x in range(start,end):
            if PrimeBenchmark.is_prime(x):
                local_primes.append(x)
        queue.put(local_primes)
        
    
    def run_single(self):
        
        start_time = time.perf_counter()

        primes = []
        for n in range(self.start,self.end):
            if self.is_prime(n):
                primes.append(n)
        elapsed = round(time.perf_counter() - start_time,5)
        return elapsed, primes
    
    def run_multi(self):
        queue = Queue()
    
    def _make_chunks(self):
        