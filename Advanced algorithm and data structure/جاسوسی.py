n = int(input())
name =[]
for i in range(n):
    name.append(input())

q = int(input())
info =[]
for i in range(q):
    info.append(input())


li =[]
counter =0
for i in info:
    if i not in li and len(li)+1<n:
        li.append(i)
    elif i in li:
        pass
    else:
        counter+=1
        li =[]
        li.append(i)

print(counter)

