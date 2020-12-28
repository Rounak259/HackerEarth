size = int(input())
num_list = list(map(str, input().split(' ')))[:size]
num = str()
for i in num_list:
    num = num+(i[-1])
num = int(num)
if num%10==0:
    print("Yes")
else:
    print("No")