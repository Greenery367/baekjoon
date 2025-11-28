T = int(input())

for t in range(1,T+1):
    txt = input()
    stack = []

    for i in txt:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
            pass
    print(f"#{t} {len(stack)}")