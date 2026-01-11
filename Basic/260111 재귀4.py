# 재귀로 중복 순열 호출하기
# 111 - 666

def recursive(depth, result):
    if depth == 3:
        print(*result)
        return
    
    for i in range(1,7):
        result.append(i)
        recursive(depth+1, result)
        result.pop()
        
recursive(0, [])