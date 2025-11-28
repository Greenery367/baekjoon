def solution(order):
    answer = 0
    txt = str(order)
    
    for i in range(len(txt)):
        if int(txt[i]) % 3 == 0 and txt[i] != '0':
            answer += 1
            
    return answer

solution(3)