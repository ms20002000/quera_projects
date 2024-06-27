n = int(input())

a = 1
b = 2
if n>2:
    for i in range(2, n):
        a, b = b, a + b
if n ==1:
    print(1)
else:
    print(b%(pow(10, 9)+7))
