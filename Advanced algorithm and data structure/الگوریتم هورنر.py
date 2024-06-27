n, x = map(int, input().split())
q = list(map(int, input().split()))
s =0
j =0
for i in range(n, -1, -1):
    s += x**i*q[j]
    j +=1
s = s%(10**9+7)
print(s)

