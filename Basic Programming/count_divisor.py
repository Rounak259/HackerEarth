count = 0
lst = [int(i) for i in input().split(' ')]
for i in range(lst[0], lst[1]+1):
    if i%lst[2]==0:
        count+=1
print(count)