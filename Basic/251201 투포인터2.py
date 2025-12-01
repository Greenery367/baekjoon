n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
start = 0
end = 0
current_sum = 0

while True:
    if current_sum >= m:
        current_sum -= arr[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += arr[end]
        end += 1
    
    if current_sum == m:
        count += 1

print(count)
