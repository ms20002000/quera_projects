n = int(input())
a = tuple(map(int,input().split()))
distance =dict()


for i,ai in enumerate(a):
    if ai in distance:
        d = i - distance[ai][0]
        if distance[ai][1]<d:
            distance[ai][1]=d
        distance[ai][0]=i
    else:
        distance[ai]=[i,i+1]
        
print(min(map(lambda x:max(x[1][1],len(a)-x[1][0]),distance.items())))