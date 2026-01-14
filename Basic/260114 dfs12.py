arr = [
    [0,1,1,1,0,0],
    [1,0,1,1,0,0],
    [1,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,1,0,0,1],
    [0,0,0,0,0,0]
]


used = [0] * 6
def dfs(now):
    used[now] = 1
    print(now, end = ' ')
    for next in range(6):
        if arr[now][next] == 1 and not used[next]:
            dfs(next)

dfs(4)