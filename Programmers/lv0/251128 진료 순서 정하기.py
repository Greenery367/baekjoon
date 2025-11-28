def solution(emergency):
    # 내림차순으로 정렬한 emergency의 순위 계산
    arr = sorted(emergency, reverse=True)
    
    # 각 원소가 내림차순으로 몇 번째 순위에 있는지 구하기
    answer = [arr.index(i) + 1 for i in emergency]
    
    return answer
