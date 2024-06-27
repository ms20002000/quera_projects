t = int(input())
li =[]

def count_two(n:int):
    counter =0
    while True:
        if n%2 ==0:
            counter +=1
            n = n/2
        else:
            return counter


def count_num(n:int, k:int):
    counter =0
    a =n
    while True:
        n = n*2
        counter +=1
        if n%k == 0:
            return counter
        elif n > k*a+1:
            return False


for i in range(t):
    n ,k = map(int, input().split())

    if n%k == 0:
        li.append(0)

    elif k%n ==0 or k%2==0:
        c = count_num(n, k)
        if c == False:
            li.append(-1)
        else:
            li.append(c)

    else:
        li.append(-1)


for i in li:
    print(i)