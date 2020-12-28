bricks = int(input())
b_count = 0
for i in range(1, bricks+1):
    b_count = b_count+i
    if b_count>=bricks:
        print("Patlu")
        break
    b_count = b_count+(2*i)
    if b_count>=bricks:
        print("Motu")
        break