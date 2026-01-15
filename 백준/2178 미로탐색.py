from collections import deque

N,M = map(int, input().split())
maze =[list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
