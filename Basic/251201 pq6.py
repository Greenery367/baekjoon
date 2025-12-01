import heapq

microbes = [
    (2,'BHC'),
    (1,'NeNe'),
    (3,'KFC'),
    (1,"BBQ"),
    (2,"Moms"),
    (4,'Mc')
]

pq = [(length, name) for length, name in microbes]
heapq.heapify(pq)

while len(pq) > 1:
    l1, n1 = heapq.heappop(pq)
    l2, n2 = heapq.heappop(pq)
    
    new_length = l1 + l2
    new_name = min(n1, n2)
    heapq.heappush(pq, (new_length, new_name))

final_length, final_name = pq[0]
print(final_name, final_length)
