for i in range(0, int(input())):
    size, rot = map(int, input().split())
    temp = list()
    arr = list(map(int, input().split(' ')))
    if rot>size:
        rot=rot%rot
    for j in range(rot, 0, -1):
        temp.append(arr[-j])
    for j in range(0, len(arr)-rot):
        temp.append(arr[j])
    for j in range(0, size):
        print(temp[j], end=' ')