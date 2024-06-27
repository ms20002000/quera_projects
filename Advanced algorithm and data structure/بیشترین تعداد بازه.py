n = int(input())
b =[]
for i in range(n):
    l = list(map(int, input().split()))
    b.append([l[0], l[1]])

b.sort(key=lambda x:x[1])
lastR =-1
final =0
for i in range(n):
    if lastR <= b[i][0]:
        lastR = b[i][1]
        final +=1

print(final)