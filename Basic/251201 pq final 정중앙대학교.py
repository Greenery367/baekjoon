import heapq
import sys
input = sys.stdin.readline

N = int(input())

# 최대힙(왼쪽), 최소힙(오른쪽)
left_heap = [-500]
right_heap = [500]

for _ in range(N):
    a, b = map(int, input().split())
    for score in [a, b]:
        if score <= -left_heap[0]:
            heapq.heappush(left_heap, -score)
        else:
            heapq.heappush(right_heap, score)
    
    # 힙 크기 조정
    while len(left_heap) > len(right_heap):
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
    while len(right_heap) > len(left_heap) + 1:
        heapq.heappush(left_heap, -heapq.heappop(right_heap))
    
    print(right_heap[0])
