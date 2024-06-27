n, k = map(int, input().split())

band_status = ['FREE' for x in range(k)]

airplane_in_airport =[]
for i in range(n):
    airplane_in_airport.append(input())

q = int(input())
orders =[]
for i in range(q):
    orders.append(input().split())

airplane_taking_off = []
airplane_landing = []

def check_status_airplane(plane_number:str):
    if plane_number in airplane_in_airport:
        return 1
    elif plane_number in airplane_taking_off:
        return 2
    elif plane_number in airplane_landing:
        return 3
    else:
        return 4

def band_status_f(number_of_band):
    return band_status[int(number_of_band)-1]

def check_band_at_fist(plane_number:str):
    flag =0
    for i in range(len(band_status)):
        if band_status[i] == 'FREE':
            band_status[i] = plane_number
            airplane_taking_off.append(plane_number)
            airplane_in_airport.remove(plane_number)
            flag =1
            break
    if flag ==0:
        print('NO FREE BOUND')



def check_band_at_end(plane_number:str):
    flag =0
    for i in range(len(band_status)-1, -1, -1):
        if band_status[i] == 'FREE':
            band_status[i] = plane_number
            airplane_landing.append(plane_number)
            flag =1
            break
    if flag ==0:
        print('NO FREE BOUND')

def take_off(plane_number:str):
    if check_status_airplane(plane_number) ==1:
        check_band_at_fist(plane_number)
    elif check_status_airplane(plane_number) ==2:
        print('YOU ARE TAKING OFF')
    elif check_status_airplane(plane_number) ==3:
        print('YOU ARE LANDING NOW')
    elif check_status_airplane(plane_number) ==4:
        print('YOU ARE NOT HERE')

def landing(plane_number):
    if check_status_airplane(plane_number) ==1:
        print('YOU ARE HERE')
    elif check_status_airplane(plane_number) ==2:
        print('YOU ARE TAKING OFF')
    elif check_status_airplane(plane_number) ==3:
        print('YOU ARE LANDING NOW')
    elif check_status_airplane(plane_number) ==4:
        check_band_at_end(plane_number)



for i in orders:
    if i[0] == 'TAKE-OFF':
        take_off(i[1])
    elif i[0] == 'PLANE-STATUS':
        print(check_status_airplane(i[1]))
    elif i[0] == 'BAND-STATUS':
        print(band_status_f(i[1]))
    elif i[0] == 'LANDING':
        landing(i[1])



