def solve(depth):
    if depth == 6:
        return
    
    print(depth, end=' ')
    solve(depth+1)
    print(depth, end= ' ')
    
solve(0)