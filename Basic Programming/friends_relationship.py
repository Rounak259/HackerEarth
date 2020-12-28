for i in range(0, int(input())):
    a = int(input())
    for j in range(1, a+1):
        print('*'*j+'#'*((2*a)-(2*j))+'*'*j)
    print('\n')