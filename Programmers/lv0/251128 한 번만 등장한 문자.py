def solution(s):
    answer = ''
    dat = [0]*123
    arr = []
    
    for i in range(len(s)):
        var = ord(s[i])
        dat[var] += 1
        
    for j in range(len(dat)):
        if dat[j] == 1:
            arr.append(j)
    
    arr.sort()
    
    for k in arr:
        answer += chr(k)
        
    print(answer)
    return answer

solution('hello')