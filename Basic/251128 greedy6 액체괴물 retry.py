n = int(input())
arr = list(map(int, input().split()))

now = 0
result = 0

for i in range(len(arr)):
    arr.sort()
    if len(arr) > 1:
        now = arr[0] + arr[1]
        arr.remove(arr[0])
        arr.remove(arr[0])
        arr.append(now)
        result += now
    else:
        break
print(result)