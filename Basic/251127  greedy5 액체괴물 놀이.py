import heapq

n = int(input())
weights = list(map(int, input().split()))

heapq.heapify(weights)

total_time = 0

while len(weights) > 1:
    a = heapq.heappop(weights)
    b = heapq.heappop(weights)

    merge_time = a+b
    total_time += merge_time

    heapq.heappush(weights, merge_time)

print(total_time)