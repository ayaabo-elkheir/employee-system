def pytable():

    n = int(input("enter number"))
    table = []

    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        table.append(row)

    for row in table:
        print(row)
pytable()