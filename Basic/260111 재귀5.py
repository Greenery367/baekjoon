n = int(input())
used = [False] * 7

def recursive(depth, result):
    if depth == n:
        print(*result)
        return
    
    for i in range(1, 7):
        # [수정 포인트] i in used 가 아니라 used[i] 를 직접 확인합니다.
        if used[i]: 
            continue # 이미 사용 중(True)이면 건너뜀
            
        used[i] = True
        result.append(i)
        recursive(depth + 1, result)
        
        # 백트래킹: 상태 복구
        result.pop()
        used[i] = False

recursive(0, [])