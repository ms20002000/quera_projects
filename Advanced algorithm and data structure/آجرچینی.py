n = int(input())
from time import time

# time1 = time()
a = [1,1,1,2]
for j in range(4, 100001):
    a.append(a[j - 1] + a[j - 2] + a[j - 3] - a[j - 4])
# time2 = time()
# print(time2-time1)
answer =[]
for i in range(n):
    q = int(input())
    answer.append(a[q]%(10**9+7))

for i in answer:
    print(i)
