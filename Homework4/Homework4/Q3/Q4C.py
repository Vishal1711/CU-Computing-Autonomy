import threading, time

listofstartingpt, listOfEndPts, listOfSums=list() ,list(), list()

start = time.time()
def prime(start,end):
    sum = 0
    global listOfSums
    for num in range(start, end + 1):

        i = 2

        for i in range(2, num):
            if (int(num % i) == 0):
                i = num
                break;

        #If the number is prime then add it.
        if i is not num:
            sum += num

    listOfSums.append(sum)

# listofstartingpt, listOfEndPts=list() ,list()
portion=1000
nth_prime=1000000
step=int(nth_prime/portion)
for i in range(1,nth_prime,step):
    # print(i)
    listofstartingpt.append(i)
    if i > 1:
        listOfEndPts.append(i-1)

listOfEndPts.append(nth_prime)
print('start pts', len(listofstartingpt) ,'\n'
        'end pts', len(listOfEndPts))

def generate_thread(start_pt,end_pt):

    t= threading.Thread(target=prime, args=(start_pt,end_pt))
    t.start()
    t.join()
for (i ,j) in zip(listofstartingpt,listOfEndPts):
    if j is not None:
        generate_thread(i,j)
        pass

    elif j is None:
        j=listOfEndPts[-1]
        generate_thread(i,j)
    print(i,j)

total=0

for ele in range(0, len(listOfSums)):
    total = total + listOfSums[ele]

print('total is',total)

end = time.time()
print("The time :", end-start)
# import threading, time
#
# listofstartingpt, listOfEndPts, lissOfD=list() ,list(), list()
#
# start = time.time()
# def prime(start,end):
#     d =0
#     b= start
#     global lissOfD
#     while b<end:
#         b=b+1
#         x = 0.0
#         a = 0
#         while x<b:
#             x=x+1
#             if (b/x)-int(b/x) == 0.0:
#                 a=a+1
#         if a==2:
#             d=d+b
#
#     lissOfD.append(d)
#     return lissOfD
#
#
# # listofstartingpt, listOfEndPts=list() ,list()
# portion=1
# nth_prime=100
# step=int(nth_prime/portion)
# for i in range(1,nth_prime,step):
#     # print(i)
#     listofstartingpt.append(i)
#     if i > 1:
#         listOfEndPts.append(i-1)
#
# print('start pts', len(listofstartingpt) ,'\n'
#         'end pts', len(listOfEndPts))
#
# def generate_thread(start_pt,end_pt):
#
#     t= threading.Thread(target=prime, args=(start_pt,end_pt))
#     t.start()
#
# for (i ,j) in zip(listofstartingpt,listOfEndPts):
#     generate_thread(i,j)
#     print(i,j)
# total=0
#
# for ele in range(0, len(lissOfD)):
#     total = total + lissOfD[ele]
#
# print('total is',total)
#
# end = time.time()
# print("The time :", end-start)
# import concurrent.futures
# import time
#
# start = time.time()
# b=1
# d = 0
#
# def prime(n):
#     d =0
#     b= 1
#     while b<n:
#         b=b+1
#         x = 0.0
#         a = 0
#
#         while x<b:
#             x=x+1
#             if (b/x)-int(b/x) == 0.0:
#                 a=a+1
#         if a==2:
#             d=d+b
#
#     return(d)
#
#
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(prime, 100000)
#     print(f1.result())
# # X = threading.Thread(target=prime, args=(10000,))
# # X.start()
# # X.join()
#
#
# end = time.time()
# print("The time :", end-start)
