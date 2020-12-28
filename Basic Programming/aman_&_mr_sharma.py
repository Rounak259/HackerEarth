toffee = 0
for i in range(0, int(input())):
    a, b = map(int, input().split())
    toffee = (toffee+1 if (2*22*a)/7<(100*b) else toffee)
print(toffee)