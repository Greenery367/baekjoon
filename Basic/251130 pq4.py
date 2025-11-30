import heapq

arr = [
    (7, 'A'),
    (9, 'C'),
    (7, 'C'),
    (6, 'D'),
    (5, 'A')
    ]

heap = []

for num, char in arr:
    heapq.heappush(heap, (char, -num))
    
sorted_arr = []
while heap:
    char, neg_num = heapq.heappop(heap)
    sorted_arr.append((-neg_num, char))

print(sorted_arr)