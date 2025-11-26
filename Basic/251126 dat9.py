criminal = [
    [5,7,9,55],
    [30,10,6,8]
]

apt = [
    [1,2,3,4],
    [5,7,10,15]
]

dat = [0]*56

# 1. DAT
for i in range(len(criminal)):
    for j in range(len(criminal[0])):
        current_criminal = criminal[i][j]
        dat[current_criminal] += 1

# 2. total
total = 0

for k in range(len(apt)):
    for f in range(len(apt[0])):
        current_apt = apt[k][f]
        if dat[current_apt] > 0:
            total += 1

all = 8
nice = all - total

print(total, nice)