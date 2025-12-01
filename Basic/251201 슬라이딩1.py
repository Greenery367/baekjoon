arr = [4,5,1,1,5,4,-3,-13,9,20,13]

def get_sum(index):
    window_sum = sum(arr[index:index+5])
    return window_sum

idx = int(input())
print(get_sum(idx))