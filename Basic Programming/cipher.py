mes = input()
key = int(input())
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symb = [':', '-', '.']
encr_mes = str()
for i in range(0, len(mes)):
    if mes[i] in num:
        encr_mes+=str((int(mes[i])+key)%10)
    elif mes[i] in symb:
        encr_mes+=mes[i]
    else:
        a = ord(mes[i])
        if a>64 and a<91:
            a+=((key%26))
            if a>90:
                a=64+(a-90)
        elif a>96 and a<123:
            a+=((key%26))
            if a>122:
                a=96+(a-122)
        encr_mes+=chr(a)
print(encr_mes)