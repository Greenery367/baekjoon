from collections import deque

T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    
    # 대기실에 줄 서 있는 피자들의 명단
    # emumerate로 피자 번호+ 양을 함께 저장
    pizzas = deque([[i+1,p] for i, p in enumerate(cheese)])
    # 화덕
    oven = deque()
    # 화덕 크기만큼 피자를 꺼내 오븐에 넣음
    for _ in range(N):
        if pizzas:
            oven.append(pizzas.popleft())

    while len(oven) > 1:
        now = oven.popleft()
        now[1] //= 2
        if now[1] == 0:
            if pizzas:
                oven.append(pizzas.popleft())
        else:
            oven.append(now)
    
    print(f"{i} {oven[0][0]}")