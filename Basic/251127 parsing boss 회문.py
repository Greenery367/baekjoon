T = int(input())

for t in range(T):
    n,m = map(int, input().split())
    arr = [list(input().split()) for _ in range(n)]

    # 세로 순회
    for i in range(n):
        # 가로 순회
        for j in range(n-m+1):
            cur = arr[i][j:j+m]
            print(cur)
            flag = True
            for k in range(m):
                print(m-k-1)
                if cur[k] != cur[m-k-1]:
                    flag = False
            if flag is True:
                print(f"#{t} {cur}")