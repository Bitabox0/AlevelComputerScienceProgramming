grid = [["x", "x", "x", "x"],
        ["x", "x", "x", "x"],
        ["x", "x", "x", "x"],
        ["x", "x", "x", "x"],
        ["x", "x", "x", "x"],
        ["x", "x", "x", "x"],]
grid[0][0] = "O"
for i in range(len(grid)):
    print(grid[i])

xAxis = int(input("please enter the row coordinate you wish to go to: "))
yAxis = int(input("please enter the column coordinate you wish to go to: "))
for i in range(len(grid)):
    for j in range(len(grid[i])):
            grid[i][j] = "x"
grid[yAxis-1][xAxis-1] = "O"

for i in range(len(grid)):
    print(grid[i])