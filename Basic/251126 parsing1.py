txt = input()
flag = True

for i in range(len(txt) // 2) :
    if txt[i] != txt[len(txt)-i] : flag = False

if flag is False : print(0)
else : print(1)