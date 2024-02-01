X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

res = [[sum(a*b for a, b in zip(xrow, ycol)) for ycol in zip(*Y)] for xrow in X]
for r in res:
     print(r)
