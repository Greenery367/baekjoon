def nth_ugly_number(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5

    for i in range(1, n):
        ugly[i] = min(next2, next3, next5)
        if ugly[i] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[i] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[i] == next5:
            i5 += 1
            next5 = ugly[i5] * 5
    return ugly

Q = int(input())
queries = list(map(int, input().split()))

max_k = max(queries)
ugly_numbers = nth_ugly_number(max_k)

results = [ugly_numbers[k-1] for k in queries]
print(*results)
