money = int(input())
arr = [500,100,50,10]
total = 0

for i in range(len(arr)):
    a = money // arr[i]
    total += a
    money = money - (a * arr[i])

print(total)