test_cases = int(input())
for test in range(1,test_cases+1):
    if test%2==1:   
        green, purple = input().split()
        green = int(green)
        purple = int(purple)
        participants = int(input())
        cost = 0
        for participant in range(0,participants):
            m, n = map(int,input().split())
            if m==1 and n==1 :
                cost = cost + green + purple
            elif n==1 and m==0 :
                cost = cost + purple
            elif m==1 and n==0:
                cost = cost + green
            else:
                cost = cost + 0
        print(cost)
    else:
        green, purple = input().split()
        green = int(green)
        purple = int(purple)
        participants = int(input())
        cost = 0
        for participant in range(0,participants):
            m, n = map(int,input().split())
            if m==1 and n==1 :
                cost = cost + green + purple
            elif n==1 and m==0 :
                cost = cost + green
            elif m==1 and n==0:
                cost = cost + purple
            else:
                cost = cost + 0
        print(cost)

#ideal code
# Write your code here
'''for i in range(int(input())):
    cost_of_green,cost_of_blue = sorted(list(map(int,input().strip().split())))
    m = 0
    n = 0
    for p in range(int(input())):
 
        a,b = list(map(int,input().strip().split()))
        if (a==1 and b==1) :
            m += 1
            n += 1
        elif a==1 and b==0:
            m += 1
        elif b == 1 and a==0:
            n +=1
    if m > n or m == n:
        print(m*cost_of_green + n*cost_of_blue)
    elif m < n :
        print(n*cost_of_green + m*cost_of_blue)'''