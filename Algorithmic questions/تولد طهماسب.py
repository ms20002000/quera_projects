n = int(input())
boresh = list(map(float, input().split()))
boresh.sort()

answer =0
for i in range(len(boresh)-1):
    if boresh[i+1] - boresh[i] > answer:
        answer = boresh[i+1] - boresh[i]

if (360-boresh[-1]) + boresh[0] > answer:
    answer = (360-boresh[-1]) + boresh[0]
print(answer/360 *100)
