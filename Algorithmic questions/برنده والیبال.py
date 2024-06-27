t = int(input())
li =[]
for i in range(t):
    n = int(input())
    s = input()
    quera =0
    codecup =0
    for j in s:
        if j == 'Q':
            quera+=1
        else:
            codecup+=1

    if quera> codecup:
        li.append('Quera')
    else:
        li.append('CodeCup')

for i in li:
    print(i)