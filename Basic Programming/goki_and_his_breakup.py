people = int(input())
min_skill = int(input())
for i in range(0, people):
    skill = int(input())
    if skill>=min_skill:
        print("YES")
    else:
        print("NO")