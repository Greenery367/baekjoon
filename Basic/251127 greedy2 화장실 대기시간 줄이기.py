arr = list(map(int, input().split()))
current_people = len(arr)-1
arr.sort()

total_time = 0

for i in range(current_people):
    total_time += current_people*arr[i]
    current_people -= 1

print(total_time)