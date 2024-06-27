n, k = map(int,input().split())
li = list(map(int, input().split()))
li = list(map(lambda x: x+1, li))
li.sort()

counter = 0
sum_li =0
for i in li:
    sum_li +=i
    if sum_li>k:
        break
    counter +=1

print(counter)
