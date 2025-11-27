arr = [
    ['ABCQ'],
    ['B[4]R'],
    ['CCDA'],
    ['BT[15]']
]

for i in arr:
    current = i[0]
    a = current.find('[')
    b = current.find(']')

    if a != -1 and b != -1:
        print(current[a+1:b], end=" ")