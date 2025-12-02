def dfs(depth, path):
    if depth == 4:
        print(' '.join(map(str,path)))
        return
    for i in range(1,4):
        dfs(depth+1, path+[i])
        
dfs(0,[])