n = int(input())
a = list(int(x) for x in input().split())[:n]
t = sum(a)
s = sorted(a)
print(a.index(8899))
try:
    for i in s:
            if (t - i)%7==0:
                print(a.index(i) if i!=0 else -1)
                break
            else:
                if s.index(i)==len(s)-1:
                    print(-1)
except:
    print(-1)