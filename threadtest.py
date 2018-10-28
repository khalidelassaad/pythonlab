"""
The following is a bit of mucking around with multi-threading
"""

import threading

lock = threading.Lock()

def grabandprint(lock, string):
    while True:
        lock.acquire()
        print(string, end="")
        input()
        lock.release()
    return None

threadA = threading.Thread(target=grabandprint, args=(lock,"A"))
threadB = threading.Thread(target=grabandprint, args=(lock,"B"))

threadA.start()
threadB.start()

grabandprint(lock, "C")

