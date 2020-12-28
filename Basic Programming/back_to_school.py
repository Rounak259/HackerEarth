a, b, c = map(int, input().split())
num = a if a>b else b
ans = num if num>c else c
print(ans)