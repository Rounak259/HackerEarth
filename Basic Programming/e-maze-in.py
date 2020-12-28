a, b = 0, 0
command = input()
for i in command:
    if i == 'L':
        a = a-1
    elif i == 'R':
        a = a+1
    elif i == 'U':
        b = b+1
    else:
        b = b-1
print(a,b)