

a = [4,2,5,3,7,6]
b = a[2:5]

n = int(input())
flag = True

for i in range(0, len(b)):
    if b[i] != a[i+n]:
        flag = False

if flag is False : print('X')
else : print('O')