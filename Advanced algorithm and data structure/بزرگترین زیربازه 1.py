n = int(input())
q = list(map(int, input().split()))
s =0
s1 =-10**9
for i in range(1,n+1):
    for j in range(n-i+1):
        for k in range(0,i):
            s += q[j+k]
        j+=i
        if s>s1:
            s1 = s
        s =0


print(s1)