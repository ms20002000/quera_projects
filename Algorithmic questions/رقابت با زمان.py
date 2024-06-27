k = int(input())
n = int(input())
apartments = list(map(int, input().split()))
apartments.insert(0, 0)
apartments.append(2*apartments[len(apartments)-1])

second =0
for i in range(1, len(apartments)):
    if abs(apartments[i] - apartments[i-1]) <= k:
        if apartments[i] - apartments[i-1] ==0:
            second +=1
            continue
        second +=2
    elif abs(apartments[i] - apartments[i-1]) % k ==0:
        second += (abs(apartments[i] - apartments[i-1]) // k ) + 1
    else:
        second += (abs(apartments[i] - apartments[i - 1]) // k) + 2

print(second-1)

