def solution(numbers, direction):
    answer = [0]*len(numbers)
    
    if direction == 'right':
        answer[0] = numbers[-1]
        for i in range(1, len(numbers)):
            answer[i] = numbers[i-1]
    elif direction == 'left':
        answer[-1] = numbers[0]
        for i in range(1, len(numbers)):
            answer[i-1] = numbers[i]
    return answer
