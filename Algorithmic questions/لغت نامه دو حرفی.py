n = int(input())
k =2
count =1
s =3
while True:
    if n<s:
        break
    k*=2
    s+=k
    count+=1
if (n-(s-k)) %2==0:
    print('a')
else:
    print('b')

