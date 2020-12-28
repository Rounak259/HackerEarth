for i in range(0, int(input())):
    str1, str2 = map(str, input().split(' '))
    if sorted(str1)==sorted(str2):
        print("YES")
    else:
        print("NO")