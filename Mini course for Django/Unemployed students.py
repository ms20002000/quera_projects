import re

def check(s:str):
    patern = r'\d*#\d*'
    if re.match(patern, s):
        return True
    else:
        return False


def solve(arr: str):
    arr = re.split(' ', arr)
    if '#' in arr[0]:
        menha = int(arr[4]) - int(arr[2])
        menha = str(menha)

        if check(arr[0]):
            st = ''
            for i in arr[0]:
                if i == '#':
                    st += '.+'
                else:
                    st += i

            if re.match(st, menha):
                s = menha + ' + ' + arr[2] + ' = ' + arr[4]
                return s
            else:
                return '-1'

        else:
            arr[0] = arr[0].replace('#','')
            if arr[0] in menha:
                s = menha+' + '+arr[2]+' = '+arr[4]
                return s
            else:
                return '-1'
    elif '#' in arr[2]:
        menha = int(arr[4]) - int(arr[0])
        menha = str(menha)

        if check(arr[2]):
            st = r''
            for i in arr[2]:
                if i == '#':
                    st += '.+'
                else:
                    st += i

            if re.match(st, menha):
                s = arr[0] + ' + ' + menha + ' = ' + arr[4]
                return s
            else:
                return '-1'

        else:
            arr[2] = arr[2].replace('#', '')
            if arr[2] in menha:
                s = arr[0] + ' + ' + menha + ' = ' + arr[4]
                return s
            else:
                return '-1'
    else:
        jam = int(arr[2]) + int(arr[0])
        jam = str(jam)

        if check(arr[4]):
            st = r''
            for i in arr[4]:
                if i == '#':
                    st += '.+'
                else:
                    st += i

            if re.match(st, jam):
                s = arr[0] + ' + ' + arr[2] + ' = ' + jam
                return s
            else:
                return '-1'

        else:
            arr[4] = arr[4].replace('#', '')
            if jam in arr[4]:
                s = arr[0] + ' + ' + arr[2] + ' = ' + jam
                return s
            else:
                return '-1'