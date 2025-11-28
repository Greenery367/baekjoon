T = int(input())  # 테스트 케이스 수

# 괄호 쌍 매칭을 위한 딕셔너리
pair = {
    '(': ')',
    '{': '}',
    '[': ']'
}

# 테스트 케이스마다 처리
for t in range(1, T + 1):  # t는 1부터 시작
    txt = input()  # 입력 받는 코드

    stack = []  # 스택을 사용하여 괄호를 처리

    for char in txt:
        if char in pair:  # 여는 괄호일 경우
            stack.append(char)
        elif char in pair.values():  # 닫는 괄호일 경우
            if stack and pair.get(stack[-1]) == char:  # 스택이 비어있지 않고, 올바른 짝인지 확인
                stack.pop()  # 짝이 맞으면 스택에서 제거
            else:
                stack.append(char)  # 짝이 맞지 않으면 스택에 넣음

    # 스택이 비어있으면 괄호 짝이 맞는 것, 비어있지 않으면 맞지 않는 것
    if not stack:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
