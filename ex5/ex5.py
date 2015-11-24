# Open file and assign it to a string
my_file = open('ss835.txt', 'r')
my_string = my_file.read()
# Trim the '\n' from the end of the string
my_string = my_string[:len(my_string)-1]
my_file.close()

# Try 4-8 colums
for cols in range(4,9):
    columns = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }
    col_len = int(len(my_string)/cols)
    i = 0
    for char in my_string:
        columns[i].append(char)
        if len(columns[i]) >= col_len:
            i += 1
    # print(columns)
    print('Columns '+ str(cols))
    for pos in range(col_len):
        for col in range(cols):
            print(columns[col][pos], end='')
    print() # new line
