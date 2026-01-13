arr = [
    [0,1,0,0,0],
    [0,0,1,1,0],
    [0,1,0,0,0],
    [0,0,0,0,0],
    [0,1,0,0,0]
]

n = int(input())

for i in range(5):
    now = arr[n-1]

    if now[i] : print(i+1)