n , k= map(int, input().split())

b =[]
a ={}
for i in range(n):
    l = list(map(int, input().split()))
    if l[1]-l[0]>0:
        b.append((l[0], l[1]))
        # a.update({l[0]: l[1]})

def mergeSort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i][0] < M[j][0]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

mergeSort(b)

for i in b:
    if k>=i[0]:
        k+=i[1] - i[0]
print(k)




