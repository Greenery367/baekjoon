from collections import deque

# 인덱스 자체가 노드의 값이 되도록 구성 (예: 0번 노드의 값은 0)
# 출력 예시: 5 3 1 2 4 0 6 순서대로 자식을 맺어줍니다.
tree = [
    [],        # 0번의 자식 (없음)
    [2],       # 1번의 자식 (2)
    [],        # 2번의 자식 (없음)
    [1, 2],    # 3번의 자식 (1, 2) -> 3 다음 1, 2가 나와야 하니까요
    [0, 6],    # 4번의 자식 (0, 6)
    [3, 1],    # 5번의 자식 (3, 1) -> 시작점 5의 자식은 3과 1
    []         # 6번의 자식 (없음)
]

# 만약 값 리스트를 따로 쓴다면 (인덱스가 0, 1, 2... 순서일 때)
value = [0, 1, 2, 3, 4, 5, 6] 

def bfs(start):
    q = deque([start])
    result = [] # 출력을 예쁘게 모으기 위해

    while q:
        now = q.popleft()
        result.append(str(now)) # 노드 번호 자체를 출력
        
        for next_node in tree[now]:
            q.append(next_node)
    
    print(" ".join(result))

# 문제의 시작점인 5번부터 출발!
bfs(5)