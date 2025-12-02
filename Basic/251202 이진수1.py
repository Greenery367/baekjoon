TC = int(input())

for t in range(1, TC+1):
    N,M = map(int, input().split())
    mask = (1 << N) -1 
    result = "ON" if (M & mask) == mask else "OFF"
    print(f"{t} {result}")