from collections import deque

T = int(input())

for t in range(1,T+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))

    queue = deque(arr)

    for m in range(M):
        a = queue.popleft()
        queue.append(a)

    print(f"#{t} {queue[0]}")