def is_valid(s):
    stack = []
    # 닫힌 괄호를 키로, 열린 괄호를 값으로 하는 딕셔너리
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        # 만약 닫힌 괄호라면?
        if char in mapping:
            # 스택에서 가장 위에 있는 요소를 꺼내보자 (비어있으면 가짜값 '#')
            top_element = stack.pop() if stack else '#'
            
            # 내 짝꿍(mapping[char])이랑 꺼낸 놈이 다르면?
            if mapping[char] != top_element:
                return False
        else:
            # 열린 괄호라면 스택에 추가!
            stack.append(char)

    # 문자열 다 돌았는데 스택에 남아있는 게 없어야 True!
    return not stack

# 테스트 데이터
test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]

for case in test_cases:
    print(f"{case} -> {is_valid(case)}")