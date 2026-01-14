arr = [
    [0,2,6,3,0,0],
    [2,0,7,4,0,0],
    [6,7,0,0,0,0],
    [3,4,2,0,0,0],
    [0,0,1,0,0,7],
    [0,0,0,0,0,0]
]

visited = [0] * 6

sta, end = map(int, input().split())

result = []

visited[sta] = 1

def dfs(now, total):

    
    if now == end :
        result.append(total)
        return
    
    for i in range(len(arr)):
        if arr[now][i] == 0 or visited[i] == 1:
            continue
        visited[i] = 1
        total += arr[now][i]

        dfs(i, total)
        visited[i] = 0
        total -= arr[now][i]


dfs(sta, 0)

print(max(result))
print(min(result))