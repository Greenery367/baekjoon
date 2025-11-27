txt = 'ABCDEFABCKKKKKABC'
flag = True
num = 0
result = 0

while flag:
    if num <= len(txt)-3:
        if txt[num:num+3] == 'ABC':
            result += 1
        num += 1
    else:
        flag = False


print(result)