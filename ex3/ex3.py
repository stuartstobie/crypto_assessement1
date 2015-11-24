from collections import Counter

# Open file and assign it to a string
my_file = open('ss835.txt', 'r')
my_string = my_file.read()
# Trim the '\n' from the end of the string
my_string = my_string[:len(my_string)-1]
my_file.close()

# First I find the most frequent letter in each position of the key using this code once
key_length = 6
pos = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: []
}
i = 0
for char in my_string:
    pos[i%6].append(char)
    i += 1

for n in pos:
    data = Counter(pos[n])
    print('Pos '+ str(n) + ': ' + str(data))

'''
Results of this:
Pos 0: Counter({'T': 19, 'H': 15, 'W': 13, 'I': 10, 'X': 10, 'P': 9, 'C': 8, 'A': 8, 'D': 8, 'G': 7, 'R': 6, 'L': 5, 'B': 4, 'Z': 4, 'V': 3, 'Q': 2, 'S': 2, 'N': 1, 'E': 1, 'Y': 1, 'K': 1, 'O': 1, 'U': 1, 'J': 1})
Pos 1: Counter({'Y': 16, 'U': 16, 'H': 13, 'I': 12, 'B': 12, 'L': 11, 'N': 10, 'C': 10, 'M': 8, 'Q': 5, 'A': 4, 'G': 4, 'X': 3, 'O': 3, 'S': 3, 'Z': 2, 'P': 2, 'E': 1, 'K': 1, 'V': 1, 'F': 1, 'D': 1, 'W': 1})
Pos 2: Counter({'G': 20, 'V': 15, 'U': 14, 'K': 13, 'P': 12, 'C': 10, 'Q': 8, 'F': 7, 'N': 5, 'J': 5, 'T': 5, 'W': 5, 'H': 3, 'I': 3, 'E': 3, 'X': 3, 'R': 2, 'O': 2, 'Y': 2, 'M': 2, 'A': 1})
Pos 3: Counter({'P': 19, 'Y': 14, 'S': 13, 'Z': 11, 'D': 11, 'T': 11, 'C': 10, 'E': 9, 'L': 6, 'X': 6, 'H': 5, 'O': 5, 'R': 3, 'F': 3, 'W': 3, 'M': 3, 'N': 2, 'V': 2, 'Q': 1, 'A': 1, 'J': 1, 'G': 1})
Pos 4: Counter({'D': 21, 'H': 18, 'S': 14, 'R': 11, 'Z': 11, 'Q': 9, 'C': 7, 'G': 7, 'E': 6, 'N': 5, 'M': 5, 'L': 4, 'O': 3, 'U': 3, 'K': 3, 'V': 3, 'F': 3, 'B': 2, 'J': 2, 'X': 1, 'A': 1, 'T': 1})
Pos 5: Counter({'V': 21, 'K': 16, 'J': 16, 'E': 13, 'Y': 12, 'Z': 11, 'R': 8, 'F': 8, 'I': 6, 'C': 5, 'P': 4, 'U': 3, 'L': 3, 'N': 3, 'D': 2, 'T': 2, 'W': 2, 'S': 2, 'B': 1, 'X': 1, 'M': 1})

Assuming the most common letter is E then,
Pos 0 is shifted 15
Pos 1 is shifted 20 or 16
Pos 2 is shifted 2
Pos 3 is shifted 11
Pos 4 is shifted 25
Pos 5 is shifted 17

Key should be PUCLZR
'''
alphabet = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

rev_alphabet = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}

# turn chars in string into list of corresponding numbers
my_chars =[]
for char in my_string:
    my_chars.append(alphabet[char])

shift = {
    0: 15,
    1: 20,
    2: 2,
    3: 11,
    4: 25,
    5: 17
}

i = 0
shifted_chars = []
for char in my_chars:
    shifted_chars.append(rev_alphabet[(char - shift[i%6])%26])
    i += 1
print(''.join(str(x) for x in shifted_chars))
