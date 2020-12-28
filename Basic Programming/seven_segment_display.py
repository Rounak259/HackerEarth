for i in range(0, int(input())):
    inp = input()
    a = 0
    segments = {0:6, 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6}
    for i in inp:
        a = a+segments[int(i)]
    ans = str()
    while a!=3 and a!=0:
        ans = ans+str(1)
        a = a-2
    if a==3:
        ans = ans+str(7)
    print(ans[::-1])