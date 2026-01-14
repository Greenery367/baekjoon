from collections import deque 

# 카드가 1~ N까지 순서대로 있음

# 1. 제일 위의 카드를 바닥에 버린다.
# 2. 그 다음 제일 위의 카드를 제일 아래 카드 밑으로 옮긴다.
# N이 주어졌을 때 가장 마지막에 남는 카드는?

n = int(input())

cards =deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])