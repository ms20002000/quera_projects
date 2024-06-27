def encode(text:str):
    words_numb = []
    words = []
    numbers =[]
    j =1
    s =''
    for i in text:
        if not i.isalnum() and i!=' ' and i!='\n':
            text = text.replace(i,'')

    for i in text:
        if i.isalnum() :
            s+=i
        elif s!='':
            if s in words:

                for k in words_numb:
                    if s == list(k.keys())[0]:
                        numbers.append(list(k.values())[0])
            else:
                words.append(s)
                words_numb.append({s:j})
                numbers.append(j)
                j+=1
            s=''

    d ={}
    for i in words_numb:
        d.update({list(i.keys())[0]: list(i.values())[0]})

    return (d, numbers)