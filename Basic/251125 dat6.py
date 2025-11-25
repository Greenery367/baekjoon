txt= 'ABCDE'
arr = list(map(str, input().split()))

print(arr)

for i in arr:
    flag = False
    for j in txt:
        if i == j : flag = True
    if flag is True : print('O', end=" ")
    else : print('X', end=" ")