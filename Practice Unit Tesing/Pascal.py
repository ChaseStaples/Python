def pascal(n):
    # Iterate through every line
    # and print entries in it
    pascalList = []
    newList = []
    for line in range(0, n):

        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1):
            pascalList.append(coef(line, i))

        print(pascalList)
        print(f"Line: {i + 1} done")
    return pascalList

def coef(x, y):
    result = 1
    if (y > x - y):
        y = x - y
    for i in range(0, y):
        result = result * (x - i)
        result = result // (i + 1)
    return result

final = pascal(6)
for x in range(len(final)):
    print(final[x], " ", end="")