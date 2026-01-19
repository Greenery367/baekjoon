from collections import deque

N,M = map(int, input().split())
maze =[list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x,y = 0, 0

q = deque()
q.append((x,y))

while q:
    x,y = q.popleft()
    if x == M-1 and y == N-1:
        print(maze[y][x])
        break

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < N  and 0 <= nx < M and maze[ny][nx] == 1:
            maze[ny][nx] = maze[y][x] + 1
            q.append((nx, ny))