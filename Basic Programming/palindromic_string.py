a = input()
for i in range(0, len(a)):
    if a[i] != a[-i-1]:
        print('NO')
        break
    elif i == len(a)/2 or i == len(a)/2+1:
        print('YES')
        break