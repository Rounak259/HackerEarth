a = int(input())
b = str(input())
if 'HH' in b:
    print("NO")
else:
    print("YES")
    print(b.replace('.', 'B'))