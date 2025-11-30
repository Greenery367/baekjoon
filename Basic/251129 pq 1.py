import heapq

arr = [5, 2, 8, 1, 9]
pq = []

for i in arr:
    heapq.heappush(pq, i)

sorted_arr = []

while pq:
    sorted_arr.append(heapq.heappop(pq))   # ← pop을 써야 함!

print(sorted_arr)
