import heapq

arr = [
    (9,'A'),
    (8,'B'),
    (9,'A'),
    (10,'C'),
    (15,'A')
]
pq = []
for num, char in arr :
    heapq.heappush(pq, (num, -ord(char), char))
    
n = len(arr)

for _ in range(n):
    num, _, char = heapq.heappop(pq)
    new_num = (num*2) % 17
    heapq.heappush (pq, (new_num, -ord(char),char))

result = []
while pq:
    num, _, char = heapq.heappop(pq)
    result.append((num, char))
print(result)