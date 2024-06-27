n = int(input())

answer =1
for i in range(n):
    a, b = map(int, input().split())
    if a == answer:
        answer =b
    elif b == answer:
        answer =a

print(answer)
