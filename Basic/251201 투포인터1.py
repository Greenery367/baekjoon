n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = n - 1
found = False

while left < right:
    total = arr[left] + arr[right]
    if total == m :
        print(left, right)
        found = True
        break
    elif total < m:
        left += 1
    else:
        right -= 1
        
if not found:
    print("찾을 수 없음")