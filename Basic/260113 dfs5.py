arr = []
arr.append([])
arr.append([])
arr.append([])

arr[0] = ['A','B','T']
arr[2] = ['R','S']

for i in range(3):
    now = arr[i]
    if now :
        num = len(now)
        for j in range(num):
            print(now[num-j-1], end='')
    print()
    