a = [[5,5,2,6], [9,1,1,3]]
tar = [5,6,1,1,1,1,5,4]

def get_count(element, target):
    N = len(element)
    M = len(element[0])

    arr = [[0 for _ in range(M)] for __ in range(N)]

    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in target:
                if k == element[i][j] : cnt += 1
            arr[i][j] = cnt

    for n in arr:
        print(*n)

get_count(a,tar)