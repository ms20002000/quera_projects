li = list(map(int, input().split()))
n = int(input())
for i in range(len(li)):
    if li[i] == n:
        if i ==0:
            print(6)
            break
        print(7- i)
        break