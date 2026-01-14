
# 여행지 개수 입력
limit = int(input())
# 여행지 정보
tour_spot = [list(map(int, input().split())) for _ in range(limit)]
# 출발, 종료 지점
sta, end = map(int, input().split())

# 방문 배열
visited = [0] * limit
visited[sta] = 1

# 여행 비용이 저장되는 배열
result = []

def dfs(now, cost):
    if now == end :
        result.append(cost)
        return
    
    for i in range(limit):
        if tour_spot[now][i] != 0 and visited[i] == 0:
            visited[i] = 1
            dfs(i, cost + tour_spot[now][i])
            visited[i] = 0

dfs(sta, 0)

print(min(result))
print(max(result))
