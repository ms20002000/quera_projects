n = int(input())
answers = input()
k = int(input())
scores =[]

def check_kelid(mark: str, answers: str):
    mark_encode = ''
    if mark.count('#')>1:
        return -1
    elif mark.count('#') == 0:
        return 0
    elif mark[0] == '#':
        mark_encode = 'A'
    elif mark[1] == '#':
        mark_encode = 'B'
    elif mark[2] == '#':
        mark_encode = 'C'
    elif mark[3] == '#':
        mark_encode = 'D'

    if mark_encode == answers:
        return 3
    else:
        return -1

for i in range(k):
    score = 0
    for j in range(n):
        mark = input()
        score += check_kelid(mark, answers[j])

    scores.append(score)


for i in scores:
    print(i)

