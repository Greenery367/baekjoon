n = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = 0
num = 0

for i in arr:
    if total + i <= 100:
        num += 1
        total += i

print(num)