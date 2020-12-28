vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(0, int(input())):
    count=0
    a = int(input())
    my_word = input().lower()
    for j in range(0, a):
        if j!=a-1:
            if my_word[j] not in vowels and my_word[j+1] in vowels:
                count+=1
    print(count)