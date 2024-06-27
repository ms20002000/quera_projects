n , c= map(int, input().split())
l = list(map(int, input().split()))
l = sorted(l, reverse=True)

for i in l:
    if i > c:
        d = i-c
        c -=d
    else:
        break
    if c<=0:
        break

if c<=0:
    print(0)
else:
    print(c)