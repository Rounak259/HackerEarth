acc_dim = int(input())
test_case = int(input())
for i in range(0, test_case):
    w, h = input().split()
    w = int(w)
    h = int(h)
    if (w==acc_dim and h==acc_dim) or (w==h and w>acc_dim):
        print("ACCEPTED")
    else:
        if w<acc_dim or h<acc_dim:
            print("UPLOAD ANOTHER")
        else:
            print("CROP IT")