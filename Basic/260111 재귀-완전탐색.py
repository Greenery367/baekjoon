import sys

# 받은 주사위의 개수
n = int(sys.stdin.readline())

# # 중복 방지 배열
# used = [False] * 7

# 10 이하가 나오는 경우의 수
total = 0

def recursive(depth, current_sum):
    global total
    
    if depth == n and current_sum <= 10:
        total += 1
        return
    
    elif depth == n:
        return
    
    for i in range(1, 7):
        current_sum += i
        recursive(depth+1, current_sum)
        current_sum -= i
                
recursive(0, 0)
print(total)