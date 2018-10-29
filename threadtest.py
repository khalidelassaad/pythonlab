"""
The following is a bit of mucking around with multi-threading
"""

import threading

lock = threading.Lock()
threadID = None

def grabandprint(lock, string):
    lock.acquire()
    print(threadID)
    lock.release()
    return None

threadA = threading.Thread(target=grabandprint, args=(lock,"A"))
threadB = threading.Thread(target=grabandprint, args=(lock,"B"))

lock.acquire()
threadA.start()
threadID = threadA.ident

threadB.start()
threadID = threadB.ident
lock.release()

threadA.join()
print("Thread A done!")

threadB.join()
print("Thread B done!")

