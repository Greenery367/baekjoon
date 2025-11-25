a = [5,7,5,4,2,9]
b = [5,4,2,5,6]

for i in range(len(a)):
    if b.count(a[i]) > 0 : print('O', end=" ")
    else : print('X', end=" ")