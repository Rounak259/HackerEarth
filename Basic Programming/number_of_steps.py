size = int(input())
a = list(map(int, input().split()))[:size]
b = list(map(int, input().split()))[:size]
num = min(a)
steps = 0
flag = True
for i in range(0, size):
    while a[i]>num and b[i]>0:
        a[i]-=b[i]
        steps+=1
    if a[i]<0:
        flag = False
    else:
        num=a[i]
for i in a:
    if i!=min(a):
        flag=False
print("-1" if flag==False else steps)