from collections import deque


# N : 1~N명
# K : 제거할 사람의 순번
N, K = map(int, input().split())

# 사람 목록
q = deque(range(1, N+1))
now = 1
result =[]

while q:
    if now == K :
        n = q.popleft()
        result.append(str(n))
        now = 1
    else:
        n = q.popleft()
        q.append(n)
        now += 1
        

print("<" + ", ".join(result) + ">")