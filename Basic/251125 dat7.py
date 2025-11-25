txt = 'BBQBHCBTS'
dat = [0 for i in range(92)]

for i in txt:
    num = ord(i)
    dat[num] += 1
print(max(dat))