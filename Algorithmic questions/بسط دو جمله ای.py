from math import factorial
n = int(input())

def rFromk(i:int, n:int):
    a = factorial(n)
    b = factorial(i)
    c = factorial(n-i)
    return a//(b*c)


li_factors =[]
for i in range(n+1):
    li_factors.append(rFromk(i, n))

counter =0
answer = f"x{'^' if i !=1 else ''}{'' if n==1 else n if n//10 ==0 else f'{{{n}}}'}+"
for i in range(n-1,0,-1):
    counter +=1
    s = (f"{li_factors[i]}x{'^' if i !=1 else ''}{'' if i==1 else i if i//10 ==0 else f'{{{i}}}'}"
         f"y{'^' if counter !=1 else ''}{'' if counter==1 else counter if counter//10 ==0 else f'{{{counter}}}'}"
         f"+")
    answer +=s

answer += f"y{'^' if n !=1 else ''}{'' if n==1 else n if n//10 ==0 else f'{{{n}}}'}"
print(answer)







