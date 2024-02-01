x = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[11, 12, 13],
     [14, 15, 16],
     [17, 18, 19]]

res = [[x[i][j] + y[i][j] for j in range (len(x[0]))] for i  in range(len(x))]

for r in res:
    print(r)