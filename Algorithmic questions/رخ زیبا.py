x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = map(int, input().split())

score =0
if x1 == x3 or x1 == x4:
    score +=1
if x2 == x3 or x2 == x4:
    score +=1
if y1 == y3 or y1 == y4:
    if x1 != x3 and x1 != x4:
        score+=1
if y2 == y3 or y2 == y4:
    if x2 != x3 and x2 != x4:
        score+=1

if score ==0 or score > 1:
    print('unhappy')
else:
    print('happy')

