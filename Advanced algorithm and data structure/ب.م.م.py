import sys
def set_recursion_limit():
    sys.setrecursionlimit(10**6)
set_recursion_limit()

def f(a, b):
    if b==0 :
        return a
    return f(b, a%b)


a, b = map(int, input().split())

if a>b:
    x = f(a,b)
else:
    x = f(b,a)

print(x)