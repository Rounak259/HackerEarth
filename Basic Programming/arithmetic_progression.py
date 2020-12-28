tn = int(input())
for _ in range(tn):
    a,b,c = list(map(int, input().strip().split()))
    print((abs((b-a)-(c-b))+1)//2)