tree = ['A','B','T','Q','V','X']
arr = [
    [0,1,1,1,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

for i in range(len(arr)):
    print(i)
    now = arr[i]
    if now.count(1):
        for i in range(6):
            if now[i] == 1:
                print(i)