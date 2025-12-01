arr = [4,5,1,1,5,4,-3,-13,9,20,13]

def get_sum():
    biggest = 0
    idx = 0
    for i in range(len(arr)-4):
        window_sum = sum(arr[i:i+5])
        if window_sum > biggest :
            biggest = window_sum
            idx = i
    return idx

print(get_sum())