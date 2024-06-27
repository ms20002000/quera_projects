n, m = map(int, input().split())

q = list(map(int, input().split()))

s =[]
for i in range(m):
    x = int(input())
    s.append(0)
    for j in range(n):
        if x>q[j]:
            s[i]+=1

for i in s:
    print(i)