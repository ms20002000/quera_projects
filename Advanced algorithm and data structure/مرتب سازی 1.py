n = int(input())
q = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i+1, n):
        if q[i] > q[j]:
            a = q[i]
            q[i] = q[j]
            q[j] = a
print(*q)
