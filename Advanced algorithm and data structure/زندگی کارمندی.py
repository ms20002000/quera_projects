n = int(input())
l = list(map(int, input().split()))
l = sorted(l)
counter =0

for i in l:
    if counter < i:
        counter+=1
print(counter)