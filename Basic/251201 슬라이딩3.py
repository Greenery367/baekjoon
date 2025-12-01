n, m = map(int, input().split())
arr = list(map(int, input().split()))

biggest = 0
idx = 0
for i in range(n-m):
    sum_v = sum(arr[i:i+m])
    if sum_v > biggest :
        biggest = sum_v
        idx = i
print(idx)