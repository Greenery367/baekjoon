import sys # 시스템 라이브러리 추가
from collections import deque

# 1. input을 sys.stdin.readline으로 교체 (속도 핵심!)
input = sys.stdin.readline

T = int(input())
q = deque()

for _ in range(T):
    n = input().split()
    cmd = n[0]
    
    if cmd == 'push':
        q.append(n[1])
    elif cmd == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        print(1 if not q else 0)
    elif cmd == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)