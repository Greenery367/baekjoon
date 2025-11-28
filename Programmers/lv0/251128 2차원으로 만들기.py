def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):  # i는 n만큼 증가
        answer.append(num_list[i:i+n])  # i부터 n개씩 잘라서 추가
    return answer
