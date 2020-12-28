nums = int(input())
num_list = list(input().split())
req_num = list()
i = 0
while i<nums/2:
    req_num.append(num_list[i][0])
    i+=1
while i<nums:
    req_num.append(num_list[i][-1])
    i+=1
num = ''.join(str(i) for i in req_num)
num = int(num)
if num%11==0:
    print("OUI")
else:
    print("NON")