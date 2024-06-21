import threading
import time
import os

def print_num():
    for i in range(1,10):
        print(i)
    print("thread-1 PID: ", os.getpid()) # process id
    print("thread-1 PPID: ", os.getppid()) # parent process id
    print("Threading name is: ", threading.current_thread().name)


def print_alph():
    for i in range(65, 75):
        print(chr(i))
    print("thread-2 PID: ", os.getpid()) # process id
    print("thread-2 PPID: ", os.getppid()) # parent process id
    print("Threading name is: ", threading.current_thread().name)
print("Start")
print("Main thread PID: ", os.getpid()) # process id
print("Threading name is: ", threading.current_thread().name)

t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_alph)

start = time.time()

t2.start()
t1.start()


t1.join()
t2.join()

end = time.time()

print("Time taken in seconds: ", end - start)

print("End")
