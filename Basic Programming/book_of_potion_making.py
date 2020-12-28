code = input()
if len(code)==10:
    code_num = list(map(int, (x for x in code)))
    num = list()
    for i, j in zip(range(1, len(code_num)+1), code_num):
        num.append(i*j)
    print("Legal ISBN" if sum(num)%11==0 else "Illegal ISBN")
else:
    print("Illegal ISBN")