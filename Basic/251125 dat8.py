ground = [[4,5,7,6],
          [1,5,5,4],
          [1,1,1,1]]
citizen = [
    [5,6,4],
    [1,5,3]
]

arr = [[0,0,0] * 2]
dat = [0] * 20

for i in ground:
    for j in i:
        dat[j] += 1

for k in range(len(citizen)):
    for l in range(len(citizen[0])):
        var = citizen[k][l]
        arr[k][l] = dat[var]

for i in range(2):
    print(arr[i])