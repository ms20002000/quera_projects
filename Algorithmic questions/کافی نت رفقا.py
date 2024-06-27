n, m = map(int, input().split())

computers = [0 for x in range(n)]
answer =[]
z =[]
def check_computers(computers:list, s:int, l:int):
    counter =0
    for i in range(s, s+l):
        if computers[i] == 1:
            counter+=1
    if counter ==0:
        return True
    else:
        return False

def fill(computers: list, s:int, l:int):
    for i in range(s, s+l):
        computers[i] =1

flag =0
for i in range(m):
    s, l = map(int, input().split())
    s -=1
    for j in range(s,n):
        if j + l > n:
            break
        if computers[j] == 0:
            check = check_computers(computers, j, l)
            if check == True:
                fill(computers, j, l)
                flag =1

        if flag ==1:
            flag=0
            break
    answer.extend(computers)


for i in range(len(answer)):
    if i%6 ==0:
        print()
        print(answer[i], ' ', end='')
        continue
    print(answer[i], ' ', end='')
