import threading
import time
start = time.time()
var = 0

def add(n):
    for i in range(n):
        global var
        var = var + 1

def minus(n):
    for i in range(n):
        global var
        var = var - 1

# for i in range(5000000):
#     add()
#     minus()

X = threading.Thread(target=add, args=(5000000,))
X.start()
X.join()
Y = threading.Thread(target=minus, args=(5000000,))
Y.start()
Y.join()
# print(threading.activeCount())
print(var)


end = time.time()
print("The time :", end-start)
