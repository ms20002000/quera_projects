import sys
def set_recursion_limit():
    sys.setrecursionlimit(10**6)
set_recursion_limit()

def zoj(x):
    if x==0:
        return 5
    return fard(x-1) -21

def fard(x):
    h = zoj(x-1)
    return h**2


n = int(input())

if n%2 == 0:
    x = zoj(n)
else:
    x = fard(n)

print(x)