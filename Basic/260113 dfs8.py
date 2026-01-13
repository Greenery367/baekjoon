arr = [
    [0,1,1,1,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

tree = ['A','B','T','Q','V','X']

n = int(input())

now = arr[n]

for i in range(6):
    if now[i] == 1:
        print(tree[i])