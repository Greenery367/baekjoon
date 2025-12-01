def solution(num_list):
    answer = [0] * len(num_list)
    for i in range(len(num_list)):
        answer[i] = num_list[len(num_list)-i-1]
    return answer