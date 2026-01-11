import sys

# 공백으로 분리하여 리스트 생성
arr = sys.stdin.readline().split()
n = len(arr)

result = 0

def solve(depth, cnt):
    global result
    
    if depth == n:
        if cnt >= 2: 
            result += 1
        return
    
    solve(depth + 1, cnt + 1)
    
    solve(depth + 1, cnt)

solve(0, 0)
print(result)