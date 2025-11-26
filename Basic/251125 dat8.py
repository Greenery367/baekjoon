ground = [[4,5,7,6],
          [1,5,5,4],
          [1,1,1,1]]
citizen = [
    [5,6,4],
    [1,5,3]
]

dat = [0] * 8

# 1. DAT 배열 생성하기
# 총 3번 세로 순회
for i in range(len(ground)):
    # 총 4번 가로 순회
    for j in range(len(ground[0])):
        # 해당 칸의 dat 배열 +1
        current = ground[i][j]
        dat[current] += 1

# 2. citizen과 대조하여 출력하기
for k in range(len(citizen)):
    for f in range(len(citizen[0])):
        current_citizen = citizen[k][f]
        print(dat[current_citizen], end=" ")
    print()
    