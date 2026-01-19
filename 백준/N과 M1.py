# 길이 = M
# 범위 = 1~N
N, M = map(int, input().split())
visited = [False] * N

def solve(depth, path):
    if depth == M:
        print(*path)
        return
    
    else:
        for i in range(N):
            if visited[i] == False: 
                path.append(i+1)
                visited[i] = True
                solve(depth+1, path)
                visited[i] = False
                path.pop()

solve(0,[])
