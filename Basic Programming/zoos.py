from collections import Counter
a = input()
b = Counter(a)
print(type(b))
if b['o']==2*b['z']:
    print('Yes')
else:
    print('No')