arr = [[1,3], [2], [0,3], [2]]
path = []
visited = [False] *4

def solve(idx):
    # 1. path에 더하기
    path.append(idx)
    visited[idx] = True
    # 2. 다음 루트 찾기
    # 1. 작은 순 정렬 방문한 적 있는가?
    now = arr[idx]
    sorted(now)
    for i in range(len(now)):
        current_node = now[i]
        if not visited[current_node]:
            solve(current_node)

solve(0)
for j in path:
    print(j)

