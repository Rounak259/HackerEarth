dist = int(input())
if dist<=5 and dist>0:
    print(int(dist/dist))
elif dist>5:
    if dist%5!=0:
        num = (dist//5)+1
        print(num)
    else:
        num = dist//5
        print(num)