import threading
import time
start = time.time()
var=0
def thread_1():
    for i in range(500000):
        global var
        var = var + 1

def thread_2():
    for i in range(500000):
        global var
        var = var - 1


t1 = threading.Thread(target=thread_1, args=(), name='Thread_1')
t1.start()
t1.join()

t2 = threading.Thread(target=thread_2, args=(), name='Thread_2')
t2.start()
t2.join()

print(var)
# print(threading.activeCount())
end = time.time()
print("The time :", end-start)
