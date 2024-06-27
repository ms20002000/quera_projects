n = int(input())
q = list(map(int, input().split()))

s1 =-10**9
for i in range(n):
    s =0
    for j in range(i, n):
        s += q[j]
        if s>s1:
            s1 = s
        


print(s1)