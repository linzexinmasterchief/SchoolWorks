data = [[1,4,7,9],
        [2,8,3,5],
        [12,13,15,19],
        [8,20,35,23]]


for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        print(data[i][j], end=' ')
    print()

for i in range(0, len(data)):
    for j in range(i, len(data[i])):
        temp = data[i][j]
        data[i][j] = data[j][i]
        data[j][i] = temp

for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        print(data[i][j], end=' ')
    print()