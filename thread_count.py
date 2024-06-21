import threading
import time

def count():
    for i in range(1, 100000):
        print(i)

def sums1():
    sums = 0
    for i in range(1, 100000):
        sums += i
    print(sums)

# Main thread
print("Start")
start = time.time()

t = threading.Thread(target=count)
t1 = threading.Thread(target=sums1)

t.start()
t1.start()

print("Main thread continue executing...")

t.join()
t1.join()

end = time.time()

print("Time taken in seconds -", end - start)

print("Main thread finished")
