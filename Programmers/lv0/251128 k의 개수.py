def solution(i, j, k):
    answer = 0
    for f in range(i, j+1):
        var = str(f)
        answer += var.count(str(k))
    print(answer)
    return answer

solution(1,13,1)