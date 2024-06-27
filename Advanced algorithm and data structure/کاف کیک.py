n , k= map(int, input().split())
l = list(map(int, input().split()))

if k==1:
    print(max(l))
elif k==2:
    for i in range(len(l)-1):
        if l[i+1] >= l[i]:
            break
    min1 = max(l[:i+1])
    min2 = max(l[i+1:])
    min3 = min(min1, min2)

    for i in range(len(l)-1, 0, -1):
        if l[i-1] >= l[i]:
            break
    min4 = max(l[i:])
    min5 = max(l[:i])
    min6 = min(min4, min5)
    print(min(min6,min3))
else:
    print(min(l))