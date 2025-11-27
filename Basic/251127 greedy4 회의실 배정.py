n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr = sorted(arr, key=lambda x:(x[1], x[1]-x[0]))

start, current = 0,0

for i in range(len(arr)):
    if start <= arr[i][0] :
        current += 1
        start = arr[i][1]

print(current)