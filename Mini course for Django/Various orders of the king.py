n = input().split()

if n[0] == 'food':
    if n[1] == 'water':
        print(0.5)
    elif n[1] == 'dinner':
        print(1.0)
    else:
        print(10.0)
elif n[0] == 'promote':
    if n[1] == 'judge':
        print(50.0)
    elif n[1] == 'minister':
        print(80.0)
    elif n[1] == 'governor':
        print(100.0)
    else:
        print(10.0)
elif n[0] == 'travel':
    if n[1] == 'ground':
        print(45.0)
    elif n[1] == 'sea':
        print(58.0)
    else:
        print(10.0)
else:
    print(10.0)