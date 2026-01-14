arr = [
    [0,1,1,1,0,0],
    [1,0,1,1,0,0],
    [1,1,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,1,0,0,1],
    [0,0,0,0,0,0]
]

used = [0]*6

goals = list(map(int, input().split()))

used[goals[0]] = 1

result = 0

def dfs(now):
    global result
    if now == goals[1]:
        result += 1
        return
    
    for i in range(6):
        if used[i] == 1 : continue
        if arr[now][i] == 0 : continue

        used[i] = 1
        dfs(i)
        used[i] = 0

dfs(goals[0])
print(result)