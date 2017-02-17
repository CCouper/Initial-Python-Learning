import threading
from queue import Queue
import time

#print_lock uses the .Lock() method to lock objects that hae been aquired
print_lock = threading.Lock()

#simple job of waiting 0.5s and then print the thread and worker
def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, worker)

#threader takes a worker object, which is a thread, from q, runs it through exampleJob
#   and then returns the task as done to q. Only 10 threads will exist as defined below
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

#create a queue list named q by using the Queue() constructor.
q=Queue()

#create 10 threads as daemons, which will cease to exist after the program exits
for x in range(10):
    t=threading.Thread(target=threader)
    t.daemon = True
    t.start()

#assign current time to variable start
start=time.time()

#put 20 workers in q. these 20 workers will
for worker in range(20):
    q.put(worker)

#wait until all threads in q terminate
q.join()

print("Entire job took:", time.time()-start)
