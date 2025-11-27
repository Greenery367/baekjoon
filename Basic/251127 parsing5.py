txt = 'B[45]AB[9994]'
total = 0

arr = ['','']
last = 0
flag = False
for i in txt:
    if i == ']':
        last += 1
        flag = False
    if flag == True:
        arr[last] += i
    if i == '[':
        flag = True

for j in arr:
    total += int(j)


print(total)
