def solution(myString, pat):
    answer = 0
    new = ''
    for i in myString:
        if i=='A':
            new += 'B'
        else:
            new+='A'
    if new.count(pat): answer = 1
    else : answer = 0
    return answer