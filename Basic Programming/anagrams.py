for i in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    for j in s1[:]:
        if j in s2:
            s1.remove(j)
            s2.remove(j)
    print(len(s1) + len(s2))