n, m = map(int, input().split())

counter =0
for i in range(1, n+1):
    if i%2 !=0:
        for j in range(m):
            counter += 1
            print(counter,' ', end='')
    else:
        counter +=m+1
        for j in range(m, 0, -1):
            counter -= 1
            print(counter,' ', end='')
        counter +=m-1
    print()

