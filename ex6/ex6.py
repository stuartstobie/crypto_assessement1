# Open file and assign it to a string
my_file = open('ss835.txt', 'r')
my_string = my_file.read()
# Trim the '\n' from the end of the string
my_string = my_string[:len(my_string)-1]
my_file.close()

# Told there are 6 colums
columns = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
}
col_len = int(len(my_string)/6)
# Read the columns
i = 0
for char in my_string:
    columns[i].append(char)
    if len(columns[i]) >= col_len:
        i += 1
# permutations of 0-6 generated here: http://textmechanic.com/Permutation-Generator.html
# this is ugly as anything
permutations = [
    [0,1,2,3,4,5],
    [0,1,2,3,5,4],
    [0,1,2,4,3,5],
    [0,1,2,4,5,3],
    [0,1,2,5,3,4],
    [0,1,2,5,4,3],
    [0,1,3,2,5,4],
    [0,1,3,2,4,5],
    [0,1,3,4,5,2],
    [0,1,3,4,2,5],
    [0,1,3,5,4,2],
    [0,1,3,5,2,4],
    [0,1,4,2,3,5],
    [0,1,4,2,5,3],
    [0,1,4,3,2,5],
    [0,1,4,3,5,2],
    [0,1,4,5,2,3],
    [0,1,4,5,3,2],
    [0,1,5,2,4,3],
    [0,1,5,2,3,4],
    [0,1,5,3,4,2],
    [0,1,5,3,2,4],
    [0,1,5,4,3,2],
    [0,1,5,4,2,3],
    [0,2,1,5,3,4],
    [0,2,1,5,4,3],
    [0,2,1,3,5,4],
    [0,2,1,3,4,5],
    [0,2,1,4,5,3],
    [0,2,1,4,3,5],
    [0,2,3,5,4,1],
    [0,2,3,5,1,4],
    [0,2,3,1,4,5],
    [0,2,3,1,5,4],
    [0,2,3,4,1,5],
    [0,2,3,4,5,1],
    [0,2,4,5,1,3],
    [0,2,4,5,3,1],
    [0,2,4,1,5,3],
    [0,2,4,1,3,5],
    [0,2,4,3,5,1],
    [0,2,4,3,1,5],
    [0,2,5,4,3,1],
    [0,2,5,4,1,3],
    [0,2,5,1,3,4],
    [0,2,5,1,4,3],
    [0,2,5,3,1,4],
    [0,2,5,3,4,1],
    [0,3,1,4,5,2],
    [0,3,1,4,2,5],
    [0,3,1,5,4,2],
    [0,3,1,5,2,4],
    [0,3,1,2,4,5],
    [0,3,1,2,5,4],
    [0,3,2,4,1,5],
    [0,3,2,4,5,1],
    [0,3,2,5,1,4],
    [0,3,2,5,4,1],
    [0,3,2,1,5,4],
    [0,3,2,1,4,5],
    [0,3,4,2,5,1],
    [0,3,4,2,1,5],
    [0,3,4,5,2,1],
    [0,3,4,5,1,2],
    [0,3,4,1,2,5],
    [0,3,4,1,5,2],
    [0,3,5,2,1,4],
    [0,3,5,2,4,1],
    [0,3,5,4,1,2],
    [0,3,5,4,2,1],
    [0,3,5,1,4,2],
    [0,3,5,1,2,4],
    [0,4,1,2,3,5],
    [0,4,1,2,5,3],
    [0,4,1,3,2,5],
    [0,4,1,3,5,2],
    [0,4,1,5,2,3],
    [0,4,1,5,3,2],
    [0,4,2,1,5,3],
    [0,4,2,1,3,5],
    [0,4,2,3,5,1],
    [0,4,2,3,1,5],
    [0,4,2,5,3,1],
    [0,4,2,5,1,3],
    [0,4,3,1,2,5],
    [0,4,3,1,5,2],
    [0,4,3,2,1,5],
    [0,4,3,2,5,1],
    [0,4,3,5,1,2],
    [0,4,3,5,2,1],
    [0,4,5,1,3,2],
    [0,4,5,1,2,3],
    [0,4,5,2,3,1],
    [0,4,5,2,1,3],
    [0,4,5,3,2,1],
    [0,4,5,3,1,2],
    [0,5,1,4,2,3],
    [0,5,1,4,3,2],
    [0,5,1,2,4,3],
    [0,5,1,2,3,4],
    [0,5,1,3,4,2],
    [0,5,1,3,2,4],
    [0,5,2,4,3,1],
    [0,5,2,4,1,3],
    [0,5,2,1,3,4],
    [0,5,2,1,4,3],
    [0,5,2,3,1,4],
    [0,5,2,3,4,1],
    [0,5,3,4,1,2],
    [0,5,3,4,2,1],
    [0,5,3,1,4,2],
    [0,5,3,1,2,4],
    [0,5,3,2,4,1],
    [0,5,3,2,1,4],
    [0,5,4,3,2,1],
    [0,5,4,3,1,2],
    [0,5,4,1,2,3],
    [0,5,4,1,3,2],
    [0,5,4,2,1,3],
    [0,5,4,2,3,1],
    [1,0,5,3,4,2],
    [1,0,5,3,2,4],
    [1,0,5,4,3,2],
    [1,0,5,4,2,3],
    [1,0,5,2,3,4],
    [1,0,5,2,4,3],
    [1,0,2,3,5,4],
    [1,0,2,3,4,5],
    [1,0,2,4,5,3],
    [1,0,2,4,3,5],
    [1,0,2,5,4,3],
    [1,0,2,5,3,4],
    [1,0,3,2,4,5],
    [1,0,3,2,5,4],
    [1,0,3,4,2,5],
    [1,0,3,4,5,2],
    [1,0,3,5,2,4],
    [1,0,3,5,4,2],
    [1,0,4,2,5,3],
    [1,0,4,2,3,5],
    [1,0,4,3,5,2],
    [1,0,4,3,2,5],
    [1,0,4,5,3,2],
    [1,0,4,5,2,3],
    [1,2,5,0,3,4],
    [1,2,5,0,4,3],
    [1,2,5,3,0,4],
    [1,2,5,3,4,0],
    [1,2,5,4,0,3],
    [1,2,5,4,3,0],
    [1,2,0,5,4,3],
    [1,2,0,5,3,4],
    [1,2,0,3,4,5],
    [1,2,0,3,5,4],
    [1,2,0,4,3,5],
    [1,2,0,4,5,3],
    [1,2,3,5,0,4],
    [1,2,3,5,4,0],
    [1,2,3,0,5,4],
    [1,2,3,0,4,5],
    [1,2,3,4,5,0],
    [1,2,3,4,0,5],
    [1,2,4,5,3,0],
    [1,2,4,5,0,3],
    [1,2,4,0,3,5],
    [1,2,4,0,5,3],
    [1,2,4,3,0,5],
    [1,2,4,3,5,0],
    [1,3,5,4,0,2],
    [1,3,5,4,2,0],
    [1,3,5,0,4,2],
    [1,3,5,0,2,4],
    [1,3,5,2,4,0],
    [1,3,5,2,0,4],
    [1,3,0,4,2,5],
    [1,3,0,4,5,2],
    [1,3,0,5,2,4],
    [1,3,0,5,4,2],
    [1,3,0,2,5,4],
    [1,3,0,2,4,5],
    [1,3,2,4,5,0],
    [1,3,2,4,0,5],
    [1,3,2,5,4,0],
    [1,3,2,5,0,4],
    [1,3,2,0,4,5],
    [1,3,2,0,5,4],
    [1,3,4,2,0,5],
    [1,3,4,2,5,0],
    [1,3,4,5,0,2],
    [1,3,4,5,2,0],
    [1,3,4,0,5,2],
    [1,3,4,0,2,5],
    [1,4,5,2,3,0],
    [1,4,5,2,0,3],
    [1,4,5,3,2,0],
    [1,4,5,3,0,2],
    [1,4,5,0,2,3],
    [1,4,5,0,3,2],
    [1,4,0,2,5,3],
    [1,4,0,2,3,5],
    [1,4,0,3,5,2],
    [1,4,0,3,2,5],
    [1,4,0,5,3,2],
    [1,4,0,5,2,3],
    [1,4,2,0,3,5],
    [1,4,2,0,5,3],
    [1,4,2,3,0,5],
    [1,4,2,3,5,0],
    [1,4,2,5,0,3],
    [1,4,2,5,3,0],
    [1,4,3,0,5,2],
    [1,4,3,0,2,5],
    [1,4,3,2,5,0],
    [1,4,3,2,0,5],
    [1,4,3,5,2,0],
    [1,4,3,5,0,2],
    [1,5,4,0,2,3],
    [1,5,4,0,3,2],
    [1,5,4,2,0,3],
    [1,5,4,2,3,0],
    [1,5,4,3,0,2],
    [1,5,4,3,2,0],
    [1,5,0,4,3,2],
    [1,5,0,4,2,3],
    [1,5,0,2,3,4],
    [1,5,0,2,4,3],
    [1,5,0,3,2,4],
    [1,5,0,3,4,2],
    [1,5,2,4,0,3],
    [1,5,2,4,3,0],
    [1,5,2,0,4,3],
    [1,5,2,0,3,4],
    [1,5,2,3,4,0],
    [1,5,2,3,0,4],
    [1,5,3,4,2,0],
    [1,5,3,4,0,2],
    [1,5,3,0,2,4],
    [1,5,3,0,4,2],
    [1,5,3,2,0,4],
    [1,5,3,2,4,0],
    [2,0,4,3,5,1],
    [2,0,4,3,1,5],
    [2,0,4,5,3,1],
    [2,0,4,5,1,3],
    [2,0,4,1,3,5],
    [2,0,4,1,5,3],
    [2,0,5,3,1,4],
    [2,0,5,3,4,1],
    [2,0,5,4,1,3],
    [2,0,5,4,3,1],
    [2,0,5,1,4,3],
    [2,0,5,1,3,4],
    [2,0,1,3,4,5],
    [2,0,1,3,5,4],
    [2,0,1,4,3,5],
    [2,0,1,4,5,3],
    [2,0,1,5,3,4],
    [2,0,1,5,4,3],
    [2,0,3,1,5,4],
    [2,0,3,1,4,5],
    [2,0,3,4,5,1],
    [2,0,3,4,1,5],
    [2,0,3,5,4,1],
    [2,0,3,5,1,4],
    [2,1,4,0,3,5],
    [2,1,4,0,5,3],
    [2,1,4,3,0,5],
    [2,1,4,3,5,0],
    [2,1,4,5,0,3],
    [2,1,4,5,3,0],
    [2,1,5,0,4,3],
    [2,1,5,0,3,4],
    [2,1,5,3,4,0],
    [2,1,5,3,0,4],
    [2,1,5,4,3,0],
    [2,1,5,4,0,3],
    [2,1,0,5,3,4],
    [2,1,0,5,4,3],
    [2,1,0,3,5,4],
    [2,1,0,3,4,5],
    [2,1,0,4,5,3],
    [2,1,0,4,3,5],
    [2,1,3,5,4,0],
    [2,1,3,5,0,4],
    [2,1,3,0,4,5],
    [2,1,3,0,5,4],
    [2,1,3,4,0,5],
    [2,1,3,4,5,0],
    [2,3,4,5,0,1],
    [2,3,4,5,1,0],
    [2,3,4,0,5,1],
    [2,3,4,0,1,5],
    [2,3,4,1,5,0],
    [2,3,4,1,0,5],
    [2,3,5,4,1,0],
    [2,3,5,4,0,1],
    [2,3,5,0,1,4],
    [2,3,5,0,4,1],
    [2,3,5,1,0,4],
    [2,3,5,1,4,0],
    [2,3,0,4,5,1],
    [2,3,0,4,1,5],
    [2,3,0,5,4,1],
    [2,3,0,5,1,4],
    [2,3,0,1,4,5],
    [2,3,0,1,5,4],
    [2,3,1,4,0,5],
    [2,3,1,4,5,0],
    [2,3,1,5,0,4],
    [2,3,1,5,4,0],
    [2,3,1,0,5,4],
    [2,3,1,0,4,5],
    [2,4,3,1,5,0],
    [2,4,3,1,0,5],
    [2,4,3,5,1,0],
    [2,4,3,5,0,1],
    [2,4,3,0,1,5],
    [2,4,3,0,5,1],
    [2,4,5,1,0,3],
    [2,4,5,1,3,0],
    [2,4,5,3,0,1],
    [2,4,5,3,1,0],
    [2,4,5,0,3,1],
    [2,4,5,0,1,3],
    [2,4,0,1,3,5],
    [2,4,0,1,5,3],
    [2,4,0,3,1,5],
    [2,4,0,3,5,1],
    [2,4,0,5,1,3],
    [2,4,0,5,3,1],
    [2,4,1,0,5,3],
    [2,4,1,0,3,5],
    [2,4,1,3,5,0],
    [2,4,1,3,0,5],
    [2,4,1,5,3,0],
    [2,4,1,5,0,3],
    [2,5,3,0,1,4],
    [2,5,3,0,4,1],
    [2,5,3,1,0,4],
    [2,5,3,1,4,0],
    [2,5,3,4,0,1],
    [2,5,3,4,1,0],
    [2,5,4,0,3,1],
    [2,5,4,0,1,3],
    [2,5,4,1,3,0],
    [2,5,4,1,0,3],
    [2,5,4,3,1,0],
    [2,5,4,3,0,1],
    [2,5,0,4,1,3],
    [2,5,0,4,3,1],
    [2,5,0,1,4,3],
    [2,5,0,1,3,4],
    [2,5,0,3,4,1],
    [2,5,0,3,1,4],
    [2,5,1,4,3,0],
    [2,5,1,4,0,3],
    [2,5,1,0,3,4],
    [2,5,1,0,4,3],
    [2,5,1,3,0,4],
    [2,5,1,3,4,0],
    [3,0,2,4,5,1],
    [3,0,2,4,1,5],
    [3,0,2,5,4,1],
    [3,0,2,5,1,4],
    [3,0,2,1,4,5],
    [3,0,2,1,5,4],
    [3,0,4,2,1,5],
    [3,0,4,2,5,1],
    [3,0,4,5,1,2],
    [3,0,4,5,2,1],
    [3,0,4,1,5,2],
    [3,0,4,1,2,5],
    [3,0,5,2,4,1],
    [3,0,5,2,1,4],
    [3,0,5,4,2,1],
    [3,0,5,4,1,2],
    [3,0,5,1,2,4],
    [3,0,5,1,4,2],
    [3,0,1,2,5,4],
    [3,0,1,2,4,5],
    [3,0,1,4,5,2],
    [3,0,1,4,2,5],
    [3,0,1,5,4,2],
    [3,0,1,5,2,4],
    [3,1,2,0,4,5],
    [3,1,2,0,5,4],
    [3,1,2,4,0,5],
    [3,1,2,4,5,0],
    [3,1,2,5,0,4],
    [3,1,2,5,4,0],
    [3,1,4,0,5,2],
    [3,1,4,0,2,5],
    [3,1,4,2,5,0],
    [3,1,4,2,0,5],
    [3,1,4,5,2,0],
    [3,1,4,5,0,2],
    [3,1,5,0,2,4],
    [3,1,5,0,4,2],
    [3,1,5,2,0,4],
    [3,1,5,2,4,0],
    [3,1,5,4,0,2],
    [3,1,5,4,2,0],
    [3,1,0,5,4,2],
    [3,1,0,5,2,4],
    [3,1,0,2,4,5],
    [3,1,0,2,5,4],
    [3,1,0,4,2,5],
    [3,1,0,4,5,2],
    [3,2,1,5,0,4],
    [3,2,1,5,4,0],
    [3,2,1,0,5,4],
    [3,2,1,0,4,5],
    [3,2,1,4,5,0],
    [3,2,1,4,0,5],
    [3,2,4,5,1,0],
    [3,2,4,5,0,1],
    [3,2,4,0,1,5],
    [3,2,4,0,5,1],
    [3,2,4,1,0,5],
    [3,2,4,1,5,0],
    [3,2,5,4,0,1],
    [3,2,5,4,1,0],
    [3,2,5,0,4,1],
    [3,2,5,0,1,4],
    [3,2,5,1,4,0],
    [3,2,5,1,0,4],
    [3,2,0,4,1,5],
    [3,2,0,4,5,1],
    [3,2,0,5,1,4],
    [3,2,0,5,4,1],
    [3,2,0,1,5,4],
    [3,2,0,1,4,5],
    [3,4,1,2,5,0],
    [3,4,1,2,0,5],
    [3,4,1,5,2,0],
    [3,4,1,5,0,2],
    [3,4,1,0,2,5],
    [3,4,1,0,5,2],
    [3,4,2,1,0,5],
    [3,4,2,1,5,0],
    [3,4,2,5,0,1],
    [3,4,2,5,1,0],
    [3,4,2,0,5,1],
    [3,4,2,0,1,5],
    [3,4,5,1,2,0],
    [3,4,5,1,0,2],
    [3,4,5,2,1,0],
    [3,4,5,2,0,1],
    [3,4,5,0,1,2],
    [3,4,5,0,2,1],
    [3,4,0,1,5,2],
    [3,4,0,1,2,5],
    [3,4,0,2,5,1],
    [3,4,0,2,1,5],
    [3,4,0,5,2,1],
    [3,4,0,5,1,2],
    [3,5,1,0,2,4],
    [3,5,1,0,4,2],
    [3,5,1,2,0,4],
    [3,5,1,2,4,0],
    [3,5,1,4,0,2],
    [3,5,1,4,2,0],
    [3,5,2,0,4,1],
    [3,5,2,0,1,4],
    [3,5,2,1,4,0],
    [3,5,2,1,0,4],
    [3,5,2,4,1,0],
    [3,5,2,4,0,1],
    [3,5,4,0,1,2],
    [3,5,4,0,2,1],
    [3,5,4,1,0,2],
    [3,5,4,1,2,0],
    [3,5,4,2,0,1],
    [3,5,4,2,1,0],
    [3,5,0,4,2,1],
    [3,5,0,4,1,2],
    [3,5,0,1,2,4],
    [3,5,0,1,4,2],
    [3,5,0,2,1,4],
    [3,5,0,2,4,1],
    [4,0,1,3,5,2],
    [4,0,1,3,2,5],
    [4,0,1,5,3,2],
    [4,0,1,5,2,3],
    [4,0,1,2,3,5],
    [4,0,1,2,5,3],
    [4,0,2,3,1,5],
    [4,0,2,3,5,1],
    [4,0,2,5,1,3],
    [4,0,2,5,3,1],
    [4,0,2,1,5,3],
    [4,0,2,1,3,5],
    [4,0,3,2,5,1],
    [4,0,3,2,1,5],
    [4,0,3,5,2,1],
    [4,0,3,5,1,2],
    [4,0,3,1,2,5],
    [4,0,3,1,5,2],
    [4,0,5,2,1,3],
    [4,0,5,2,3,1],
    [4,0,5,3,1,2],
    [4,0,5,3,2,1],
    [4,0,5,1,3,2],
    [4,0,5,1,2,3],
    [4,1,0,2,3,5],
    [4,1,0,2,5,3],
    [4,1,0,3,2,5],
    [4,1,0,3,5,2],
    [4,1,0,5,2,3],
    [4,1,0,5,3,2],
    [4,1,2,0,5,3],
    [4,1,2,0,3,5],
    [4,1,2,3,5,0],
    [4,1,2,3,0,5],
    [4,1,2,5,3,0],
    [4,1,2,5,0,3],
    [4,1,3,0,2,5],
    [4,1,3,0,5,2],
    [4,1,3,2,0,5],
    [4,1,3,2,5,0],
    [4,1,3,5,0,2],
    [4,1,3,5,2,0],
    [4,1,5,0,3,2],
    [4,1,5,0,2,3],
    [4,1,5,2,3,0],
    [4,1,5,2,0,3],
    [4,1,5,3,2,0],
    [4,1,5,3,0,2],
    [4,2,0,5,1,3],
    [4,2,0,5,3,1],
    [4,2,0,1,5,3],
    [4,2,0,1,3,5],
    [4,2,0,3,5,1],
    [4,2,0,3,1,5],
    [4,2,1,5,3,0],
    [4,2,1,5,0,3],
    [4,2,1,0,3,5],
    [4,2,1,0,5,3],
    [4,2,1,3,0,5],
    [4,2,1,3,5,0],
    [4,2,3,5,0,1],
    [4,2,3,5,1,0],
    [4,2,3,0,5,1],
    [4,2,3,0,1,5],
    [4,2,3,1,5,0],
    [4,2,3,1,0,5],
    [4,2,5,3,1,0],
    [4,2,5,3,0,1],
    [4,2,5,0,1,3],
    [4,2,5,0,3,1],
    [4,2,5,1,0,3],
    [4,2,5,1,3,0],
    [4,3,0,2,5,1],
    [4,3,0,2,1,5],
    [4,3,0,5,2,1],
    [4,3,0,5,1,2],
    [4,3,0,1,2,5],
    [4,3,0,1,5,2],
    [4,3,1,2,0,5],
    [4,3,1,2,5,0],
    [4,3,1,5,0,2],
    [4,3,1,5,2,0],
    [4,3,1,0,5,2],
    [4,3,1,0,2,5],
    [4,3,2,1,5,0],
    [4,3,2,1,0,5],
    [4,3,2,5,1,0],
    [4,3,2,5,0,1],
    [4,3,2,0,1,5],
    [4,3,2,0,5,1],
    [4,3,5,1,0,2],
    [4,3,5,1,2,0],
    [4,3,5,2,0,1],
    [4,3,5,2,1,0],
    [4,3,5,0,2,1],
    [4,3,5,0,1,2],
    [4,5,0,1,2,3],
    [4,5,0,1,3,2],
    [4,5,0,2,1,3],
    [4,5,0,2,3,1],
    [4,5,0,3,1,2],
    [4,5,0,3,2,1],
    [4,5,1,0,3,2],
    [4,5,1,0,2,3],
    [4,5,1,2,3,0],
    [4,5,1,2,0,3],
    [4,5,1,3,2,0],
    [4,5,1,3,0,2],
    [4,5,2,0,1,3],
    [4,5,2,0,3,1],
    [4,5,2,1,0,3],
    [4,5,2,1,3,0],
    [4,5,2,3,0,1],
    [4,5,2,3,1,0],
    [4,5,3,0,2,1],
    [4,5,3,0,1,2],
    [4,5,3,1,2,0],
    [4,5,3,1,0,2],
    [4,5,3,2,1,0],
    [4,5,3,2,0,1],
    [5,0,4,3,1,2],
    [5,0,4,3,2,1],
    [5,0,4,1,3,2],
    [5,0,4,1,2,3],
    [5,0,4,2,3,1],
    [5,0,4,2,1,3],
    [5,0,1,3,2,4],
    [5,0,1,3,4,2],
    [5,0,1,4,2,3],
    [5,0,1,4,3,2],
    [5,0,1,2,4,3],
    [5,0,1,2,3,4],
    [5,0,2,3,4,1],
    [5,0,2,3,1,4],
    [5,0,2,4,3,1],
    [5,0,2,4,1,3],
    [5,0,2,1,3,4],
    [5,0,2,1,4,3],
    [5,0,3,2,1,4],
    [5,0,3,2,4,1],
    [5,0,3,4,1,2],
    [5,0,3,4,2,1],
    [5,0,3,1,4,2],
    [5,0,3,1,2,4],
    [5,1,4,2,3,0],
    [5,1,4,2,0,3],
    [5,1,4,3,2,0],
    [5,1,4,3,0,2],
    [5,1,4,0,2,3],
    [5,1,4,0,3,2],
    [5,1,0,2,4,3],
    [5,1,0,2,3,4],
    [5,1,0,3,4,2],
    [5,1,0,3,2,4],
    [5,1,0,4,3,2],
    [5,1,0,4,2,3],
    [5,1,2,0,3,4],
    [5,1,2,0,4,3],
    [5,1,2,3,0,4],
    [5,1,2,3,4,0],
    [5,1,2,4,0,3],
    [5,1,2,4,3,0],
    [5,1,3,0,4,2],
    [5,1,3,0,2,4],
    [5,1,3,2,4,0],
    [5,1,3,2,0,4],
    [5,1,3,4,2,0],
    [5,1,3,4,0,2],
    [5,2,4,0,1,3],
    [5,2,4,0,3,1],
    [5,2,4,1,0,3],
    [5,2,4,1,3,0],
    [5,2,4,3,0,1],
    [5,2,4,3,1,0],
    [5,2,0,4,3,1],
    [5,2,0,4,1,3],
    [5,2,0,1,3,4],
    [5,2,0,1,4,3],
    [5,2,0,3,1,4],
    [5,2,0,3,4,1],
    [5,2,1,4,0,3],
    [5,2,1,4,3,0],
    [5,2,1,0,4,3],
    [5,2,1,0,3,4],
    [5,2,1,3,4,0],
    [5,2,1,3,0,4],
    [5,2,3,4,1,0],
    [5,2,3,4,0,1],
    [5,2,3,0,1,4],
    [5,2,3,0,4,1],
    [5,2,3,1,0,4],
    [5,2,3,1,4,0],
    [5,3,4,2,0,1],
    [5,3,4,2,1,0],
    [5,3,4,0,2,1],
    [5,3,4,0,1,2],
    [5,3,4,1,2,0],
    [5,3,4,1,0,2],
    [5,3,0,2,1,4],
    [5,3,0,2,4,1],
    [5,3,0,4,1,2],
    [5,3,0,4,2,1],
    [5,3,0,1,4,2],
    [5,3,0,1,2,4],
    [5,3,1,2,4,0],
    [5,3,1,2,0,4],
    [5,3,1,4,2,0],
    [5,3,1,4,0,2],
    [5,3,1,0,2,4],
    [5,3,1,0,4,2],
    [5,3,2,1,0,4],
    [5,3,2,1,4,0],
    [5,3,2,4,0,1],
    [5,3,2,4,1,0],
    [5,3,2,0,4,1],
    [5,3,2,0,1,4],
    [5,4,3,1,2,0],
    [5,4,3,1,0,2],
    [5,4,3,2,1,0],
    [5,4,3,2,0,1],
    [5,4,3,0,1,2],
    [5,4,3,0,2,1],
    [5,4,0,1,3,2],
    [5,4,0,1,2,3],
    [5,4,0,2,3,1],
    [5,4,0,2,1,3],
    [5,4,0,3,2,1],
    [5,4,0,3,1,2],
    [5,4,1,0,2,3],
    [5,4,1,0,3,2],
    [5,4,1,2,0,3],
    [5,4,1,2,3,0],
    [5,4,1,3,0,2],
    [5,4,1,3,2,0],
    [5,4,2,0,3,1],
    [5,4,2,0,1,3],
    [5,4,2,1,3,0],
    [5,4,2,1,0,3],
    [5,4,2,3,1,0],
    [5,4,2,3,0,1],
]

# print colums in all possible arrangemnts
for arrangement in range(len(permutations)):
    print(permutations[arrangement])
    for pos in range(col_len):
        for col in permutations[arrangement]:
            print(columns[col][pos], end='')
    print()


#http://textmechanic.com/Permutation-Generator.html