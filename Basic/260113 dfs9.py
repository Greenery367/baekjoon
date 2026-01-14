tree = ['A', 'B', 'T', 'Q', 'V', 'X']
arr = [
    [0, 1, 1, 1, 0, 0], # A의 자식: B(1), T(2), Q(3)
    [0, 0, 0, 0, 1, 1], # B의 자식: V(4), X(5)
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

path = []

def solve(idx):
    # 1. 입장하자마자 내 이름을 기록함 (A -> B -> V ...)
    path.append(idx) 
    
    # 2. 내 자식들을 찾음
    for i in range(len(arr[idx])):
        if arr[idx][i] == 1:
            solve(i) # 자식으로 이동
            
            # (옵션) 만약 "돌아오는 경로"도 기록하고 싶다면 여기에 추가
            # path.append(tree[idx])

solve(0)
print(*path)