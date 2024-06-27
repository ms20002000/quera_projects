n = int(input())
a = list(map(int, input().split()))

answer = a[0]
maxsum = a[0]
for i in range(1,n):
    maxsum = max(maxsum + a[i], a[i])
    answer = max(answer, maxsum)


print(answer)
