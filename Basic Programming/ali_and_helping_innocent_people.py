tag = list(map(str, (input())))
vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
if tag[2] in vowels:
    print("invalid")
else:
    if (int(tag[0])+int(tag[1]))%2==0 and (int(tag[3])+int(tag[4]))%2==0 and (int(tag[4])+int(tag[5]))%2==0 and (int(tag[7])+int(tag[8]))%2==0:
        print("valid")
    else:
        print("invalid")