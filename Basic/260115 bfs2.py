from collections import deque

adj = [[0]*7 for _ in range(7)]

adj[0][1] = 1
adj[0][2] = 1
adj[0][3] = 1

adj[2][4] = 1
adj[2][5] = 1

adj[3][5] = 1
adj[3][6] = 1

visited = [False] * 7
q = deque()
q.append(0)
visited[0] = True

name = ['A', 'C', 'B', 'Q', 'T', 'P', 'R']

while q:
    now = q.popleft()
    print(name[now], end=' ')
    for i in range(7):
        if adj[now][i] == 1 and not visited[i]:
            visited[i] =True
            q.append(i)