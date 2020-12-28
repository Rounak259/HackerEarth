for i in range(0, int(input())):
    x, y, a, b = map(int, input().split(' '))
    if x*y == a+b:
        print("Yes")
    else:
        print("No")