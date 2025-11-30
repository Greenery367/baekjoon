import heapq

arr = [5,2,8,1,9]

min_heap = []

for x in arr :
    heapq.heappush(min_heap, x)
    
sorted_arr = []
while min_heap:
    sorted_arr.append(heapq.heappop(min_heap))
    
print(sorted_arr)