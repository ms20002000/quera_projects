q = int(input())
c = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(2001):
    for j in range(i+1):
        if j == 0 or j == i:
            c[i][j] = 1
        else:
            c[i][j] = (c[i-1][j] + c[i-1][j-1]) % (10**9+7)

answer =[]
for i in range(q):
    n, r = map(int, input().split())
    answer.append(c[n][r])


for i in answer:
    print(i)