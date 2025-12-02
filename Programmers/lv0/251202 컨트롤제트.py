def solution(s):
    total = 0
    s_arr = list(s.split())
    
    for i in range(len(s_arr)):
        if s_arr[i] == 'Z':
            total -= int(s_arr[i-1])
        else:
            total += int(s_arr[i])
    return total