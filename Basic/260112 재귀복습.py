

'''
[문제 조건]
1. 나무 개수: 3그루 (depth가 3이 되면 종료)
2. 선택지: 각 나무마다 [0, 1, 2]개 중 선택 가능
3. 제약 사항: 직전 나무에서 딴 개수와 '연속해서 같은 개수'는 딸 수 없음
   - 예: (1개 -> 1개) 불가능 / (1개 -> 0개 -> 1개) 가능
4. 출력: 가능한 모든 경우의 수 (정답은 12가 나와야 함)
'''
arr = [0,1,2]
result = 0

def solve(depth, prev):
    global result

    if depth == 3: 
        result += 1
        return
    
    for i in range(3):
        now = arr[i]
        if now == prev:
            continue
        else:
            solve(depth+1, now)

solve(0, -1)
print(result)