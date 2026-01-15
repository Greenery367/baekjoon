result  = []

k = int(input())

for i in range(k):
    num = int(input())

    if num == 0 and result != [] :
        result.pop()
    else:
        result.append(num)

print(sum(result))