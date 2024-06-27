n = input()
i =0
flag =0
while i<len(n)-1:
    counter =2
    adad = (ord(n[i])-64)
    while True:
        if n[i] == n[i+1] or n[i] == n[i+1].lower() or n[i] == n[i+1].upper():
            adad += (ord(n[i+1])-64) *counter
            if i+1 == len(n)-1:
                flag =1
            counter+=1
            i+=1
        else:
            break
        if flag==1:
            break
    i+=1
    print(adad, sep='', end='')
if flag ==0:
    print((ord(n[i])-64))