var = input()
total = 0
cur = ''
flag = True
arr = []

for i in var:
    if flag is False and (i != ']' and i != '}'):
        cur += i

    if i =='[' or i=='{':
        cur = ''
        flag = False

    elif i == ']' or i == '}':
        flag = True
        if i == ']':
            print(total)
            total += int(cur)
        else:
            print(total)
            total *= int(cur)

print(total)



