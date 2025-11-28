from collections import Counter

def solution(s):
    # 각 문자의 빈도 세기
    counter = Counter(s)
    
    # 빈도가 1인 문자만 필터링하고, 사전순으로 정렬
    result = sorted([char for char, count in counter.items() if count == 1])
    
    # 결과를 문자열로 반환
    return ''.join(result)
