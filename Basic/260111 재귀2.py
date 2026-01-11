# 반복문
# for i in range(1,4):
#     for j in range(1,4):
#         for f in range(1,4):
#             for k in range(1,4):
#                 print(i,j,f,k)
                

# 재귀함수
def solve(depth, result):
    if depth == 4:
        print(*result)
        return
    for i in range(1,4):
        result.append(i)
        solve(depth+1, result)
        result.pop()
        
solve(0,[])