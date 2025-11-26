apt_h, apt_w = map(int, input().split())
apt_arr = []
for _ in range(apt_h):
    apt_arr.append(list(map(int, input().split())))

cri_h, cri_w = map(int, input().split())
cri_arr = []
for __ in range(cri_h):
    cri_arr.append(list(map(int, input().split())))

dat_apt = [0] * 100000
total_cri = 0
total_people = set()

for i in range(apt_h):
    for j in range(apt_w):
        dat_apt[apt_arr[i][j]] += 1
        total_people.add(apt_arr[i][j])

total_num = len(total_people)
total_list = list(total_people)

for k in range(cri_h):
    for f in range(cri_w):
        current_cri = cri_arr[k][f]
        if dat_apt[current_cri] > 0 : total_cri += 1


nice = len(total_people) - total_cri

print(total_cri)
print(nice)