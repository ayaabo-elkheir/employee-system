def mariopyramid(rows):

    pyramid = []
    for i in range(1, rows + 1):
        pyramid.append("*" * i)

    for line in pyramid:
        print(line)
        
num_rows = int(input("enter number of rows: "))
mariopyramid(num_rows)