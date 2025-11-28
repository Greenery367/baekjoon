def solution(array):
    answer = 0
    for i in array:
        var = str(i)
        answer += var.count('7')
    return answer