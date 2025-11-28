from collections import Counter

def solution(before, after):
    # 두 문자열의 문자 빈도를 비교
    if Counter(before) == Counter(after):
        return 1
    return 0
