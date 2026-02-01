'''
Exercise 7: Producer / Consumer (Multiprocessing) Goal: One process
produces work items, multiple processes consume them.

Concepts: - Work queues - Process coordination

Constraints: - Producer sends 50 tasks - Consumers process until queue
empty

Hint: Use None as a sentinel value.
'''

from threading import Thread
from multiprocessing import Process, Queue

