
# 반복문으로 풀기
for i in range(1,4):
    for j in range(1,4):
        print(i, j)
        
# 재귀함수로 풀기
def solve(depth, result):
    if depth == 2:
        print(*result)
        return
    
    for i in range(1,4):
        result.append(i)
        solve(depth+1, result)
        result.pop()
        
solve(0, [])