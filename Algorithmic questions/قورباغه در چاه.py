t = int(input())
li = []
for i in range(t):
    li.append(list(map(int, input().split())))

def ghoorbaghe(a, b, h):
    counter =0
    c =0
    while True:
        c += a
        counter += 1
        if c >= h:
            print(counter)
            break
        c -=b
for i in li:
    ghoorbaghe(i[0], i[1], i[2])
