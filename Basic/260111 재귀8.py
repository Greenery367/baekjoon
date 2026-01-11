s = input()
total = 0

def solve(depth, path):
    global total
    
    if depth == 4:
        total += 1
        return
    
    for i in range(4):
        now = s[i] 
        
        if len(path) > 0:
            prev = path[-1]
            if (now == 'B' and prev == 'T') or (now == 'T' and prev == 'B'):
                continue
        
        path.append(now)
        solve(depth + 1, path)
        path.pop()

solve(0, [])
print(total)