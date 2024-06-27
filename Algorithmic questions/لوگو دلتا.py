n = int(input())

for i in range(n):
    if i != n-1:
        for j in range(2*n -1):
            if j == (2*n-1)//2 +i:
                print('D', end='')
            elif j == (2*n-1)//2 -i:
                print('D', end='')
            else:
                print('.', end='')
    else:
        for j in range(2*n-1):
            if j%2 ==0:
                print('D', end='')
            else:
                print('.', end='')
    print()
