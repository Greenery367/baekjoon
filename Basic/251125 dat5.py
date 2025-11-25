arr = [[1,5,10,15], [15,15,20,30]]
n = int(input())
cnt = 0

for i in arr:
    for j in i:
        if j == n : cnt += 1

print(cnt)