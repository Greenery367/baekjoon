N,M = map(int, input().split())
path = []
visited = [False] * (N+1)

def solve(depth, start):
    if depth == M :
        print(*path)
    
    else: 
        for i in range(start, N+1):
            if visited[i] == False:
                path.append(i)
                visited[i] = True
                solve(depth+1, i+1)
                visited[i] = False
                path.pop()

solve(0,1)