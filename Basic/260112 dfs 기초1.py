maze = [
    [0,0,0],
    [0,0,0],
    [0,0,1],
]

visited = [[False] * 3 for _ in range(3)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(y, x):
    if maze[y][x] == 1:
        return True
    
    visited[y][x] = True 
    
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 3 and 0 <= nx < 3 and not visited[ny][nx]:
            if dfs(ny, nx): 
                return True
                
    return False

if dfs(0,0):
    print("보물찾기 성공!")
else:
    print("보물 없어요ㅜㅜ")
