arr = [
    [0,0,0,0],
    [1,0,0,0],
    [1,1,0,0],
    [1,1,0,0]
]

arr1 = ['B', 'T', 'A', 'R']

n = int(input())

for i in range(4):
    now = arr[n]

    if now[i] : print(arr1[i])