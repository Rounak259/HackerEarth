a = 0
b = 7
for i in range(0, int(input())):
    floor_req = int(input())
    if abs(a-floor_req)==abs(b-floor_req):
        a = floor_req
        print("A")
    elif abs(a-floor_req)<abs(b-floor_req):
        a = floor_req
        print("A")
    else:
        b = floor_req
        print("B")