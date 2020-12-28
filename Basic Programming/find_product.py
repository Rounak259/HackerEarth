inputs = int(input())
a = list(input().split(' '))
product = int(1)
for i in a:
    if int(i)!=1:
        product = (product*int(i))%((10**9)+7)
    else:
        product=1
print(product)