for i in range(0, int(input())):
    n = int(input())
    try:
        while True:
            if n>0:
                if n%2==0:
                    print("YES")
                    break
                elif ((3*n)+1)%2==0:
                    print("YES")
                    break
            else:
                print("NO")
                break
    except:
        print("NO")