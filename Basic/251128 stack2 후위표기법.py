T = int(input())

for t in range(1, T+1):
    var = list(input().split())
    # 숫자
    stack = []
    flag = True
    for i in var:
        if i.isdigit():
            stack.append(i)
        else:
            if len(stack) == 0:
                flag = False
                break
            elif i == '.':
                break
            if len(stack) <= 1 and i.isdigit() is False:
                flag = False
                break
            b, a = int(stack.pop()), int(stack.pop())
            if i == '+':
                stack.append(a+b)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(a*b)
            elif i == '/':
                stack.append(a/b)

    if flag : print(f"#{t} {stack[0]}")
    else: print(f"#{t} error")