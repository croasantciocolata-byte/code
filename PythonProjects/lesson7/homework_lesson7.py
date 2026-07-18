grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(grid)):
    for j in range(len(grid)):
        print(grid[i][j], end = " ")
    print()

print("******")
even_nmb = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] % 2 == 0:
            even_nmb += 1
            print(grid[i][j], "[", i, ":", j, "]")
print("***********")
print("Even numbers:", even_nmb)


        

