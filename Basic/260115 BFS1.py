from collections import deque

alist = list([] * 7 for _ in range(7))
print(alist)
alist[5] = [3,1]
alist[3] = [2]
alist[1] = [4]
alist[4] = [0,6]

visited = [False] * 7

q = deque()
q.append(5)
visited[5] = True

while q:
    now = q.popleft()
    print(now, end=' ')

    for next in alist[now]:
        if not visited[next]:
            visited[next] = True
            q.append(next)