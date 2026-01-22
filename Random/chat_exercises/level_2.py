'''
LEVEL 2 — Scheduling & Control

Exercise 3: Periodic Worker (Threading + Event) Goal: Create a worker
thread that runs every 5 seconds and stops cleanly when signaled.

Concepts: - threading.Event - Graceful shutdown

Constraints: - No while True without sleep - Must stop within 1 second
of signal

Hint: Use event.wait(timeout) instead of time.sleep().
'''

def ex_3():
    from threading import Thread, Event
    