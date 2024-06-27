li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

counter =0
for i in range(len(li2)):
    if li1[i] == li2[i] and li1[i] == 1:
        counter+=1

print(counter)
