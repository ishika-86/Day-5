x = [[1, 2],
     [4, 5],
     [7, 8]]

res = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]

for r in res:
    print(r)