txt = [
    ['GOLDABCGOLD'],
    ['HELLOWORLD'],
    ['WHITEGOLD']
]

total = 0

for i in txt:
    cur = i[0]
    for j in range(len(cur)-3):
        if cur[j:j+4] == 'GOLD':
            total += 1

print(total)