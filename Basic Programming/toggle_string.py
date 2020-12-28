a = input()
my_char = list(a)
b = str()
for i in my_char:
    if i.isupper() is True:
        b=b+i.lower()
    else:
        b=b+i.upper()
print(b)