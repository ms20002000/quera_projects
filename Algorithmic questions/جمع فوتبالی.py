t = int(input())
li =[]
for i in range(t):
    a, b, c, d = map(int, input().split())
    if a+c > b+d:
        li.append('perspolis')
    elif b+d > a+c:
        li.append('esteghlal')
    else:
        if c > b:
            li.append('perspolis')
        elif b > c:
            li.append('esteghlal')
        else:
            li.append('penalty')

for i in li:
    print(i)