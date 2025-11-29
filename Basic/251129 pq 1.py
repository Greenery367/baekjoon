import heapq

arr = [5,2,8,1,9]
pq = []

for i in arr:
    heapq.heappush(pq, i)

sorted_arr = []

while pq:
    sorted_arr.append(heapq.heappush(pq))

print(sorted_arr)