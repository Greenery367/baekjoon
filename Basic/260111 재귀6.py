arr = ['Luffy', 'Zoro', 'Sanji']


def solve(depth, path):
    if depth == 3:
        if path:
            print(*path)
        return
    
    path.append(arr[depth])
    solve(depth+1, path)
    
    path.pop()
    solve(depth+1, path)
    
solve(0, [])
print()