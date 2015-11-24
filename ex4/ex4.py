from collections import Counter

# Open file and assign it to a string
my_file = open('ss835.txt', 'r')
my_string = my_file.read()
# Trim the '\n' from the end of the string
my_string = my_string[:len(my_string)-1]
my_file.close()

# First I find the most frequent letter in each position of the key using this code once
for key_length in range(4, 9):
    pos = {
        0: [],
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }
    i = 0
    for char in my_string:
        pos[i%key_length].append(char)
        i += 1

    print('Key length: ' + str(key_length))
    for n in pos:
        if n < key_length:
            data = Counter(pos[n])
            print('Pos '+ str(n) + ': ' + str(data))

'''
Results of this:
Key length: 4
Pos 0: Counter({'B': 24, 'M': 17, 'L': 17, 'P': 15, 'I': 14, 'A': 12, 'Q': 12, 'X': 11, 'T': 10, 'E': 10, 'V': 9, 'Z': 8, 'K': 8, 'O': 7, 'W': 6, 'C': 6, 'D': 6, 'F': 6, 'Y': 3, 'N': 3, 'J': 2, 'U': 2, 'S': 2})
Pos 1: Counter({'P': 22, 'C': 20, 'M': 16, 'Q': 15, 'J': 13, 'N': 13, 'R': 13, 'F': 12, 'B': 11, 'A': 10, 'L': 9, 'Y': 8, 'G': 8, 'X': 7, 'W': 5, 'U': 5, 'V': 5, 'E': 4, 'D': 4, 'H': 3, 'S': 2, 'O': 1, 'Z': 1, 'K': 1, 'T': 1, 'I': 1})
Pos 2: Counter({'X': 27, 'A': 14, 'G': 14, 'U': 13, 'Y': 13, 'K': 13, 'Z': 11, 'T': 11, 'B': 11, 'H': 11, 'O': 11, 'M': 9, 'R': 8, 'E': 7, 'P': 6, 'V': 5, 'W': 4, 'J': 4, 'N': 4, 'L': 4, 'S': 4, 'I': 2, 'C': 2, 'F': 2})
Pos 3: Counter({'R': 30, 'A': 15, 'L': 15, 'I': 14, 'E': 13, 'U': 11, 'N': 11, 'V': 10, 'H': 9, 'F': 9, 'W': 7, 'Y': 7, 'S': 7, 'M': 6, 'G': 6, 'X': 6, 'Q': 6, 'P': 6, 'J': 5, 'K': 4, 'Z': 3, 'O': 3, 'C': 2, 'T': 2, 'B': 2, 'D': 1})
Key length: 5
Pos 0: Counter({'P': 12, 'L': 11, 'B': 10, 'X': 10, 'F': 10, 'N': 8, 'K': 8, 'M': 8, 'U': 7, 'C': 7, 'I': 7, 'Q': 7, 'A': 6, 'R': 6, 'V': 6, 'J': 5, 'Y': 5, 'T': 5, 'E': 5, 'W': 4, 'Z': 4, 'H': 4, 'G': 4, 'S': 4, 'D': 3, 'O': 2})
Pos 1: Counter({'R': 15, 'A': 13, 'B': 12, 'L': 11, 'X': 10, 'G': 9, 'O': 9, 'M': 8, 'U': 7, 'N': 7, 'E': 7, 'P': 7, 'W': 6, 'Y': 6, 'F': 6, 'C': 5, 'H': 5, 'K': 4, 'I': 4, 'V': 4, 'J': 3, 'T': 3, 'Q': 2, 'D': 2, 'S': 2, 'Z': 1})
Pos 2: Counter({'P': 13, 'M': 11, 'R': 11, 'A': 10, 'J': 9, 'Y': 8, 'Q': 8, 'Z': 7, 'T': 7, 'E': 7, 'X': 7, 'I': 7, 'W': 6, 'B': 6, 'L': 6, 'H': 6, 'V': 6, 'C': 5, 'K': 5, 'G': 5, 'D': 4, 'O': 4, 'F': 4, 'N': 3, 'S': 2, 'U': 1})
Pos 3: Counter({'B': 12, 'M': 12, 'A': 10, 'L': 10, 'X': 10, 'P': 10, 'E': 9, 'U': 8, 'Q': 8, 'I': 8, 'N': 6, 'Z': 6, 'R': 6, 'W': 5, 'Y': 5, 'K': 5, 'S': 5, 'V': 5, 'F': 5, 'C': 4, 'T': 4, 'H': 4, 'G': 4, 'O': 4, 'J': 2, 'D': 1})
Pos 4: Counter({'X': 14, 'R': 13, 'A': 12, 'C': 9, 'M': 9, 'U': 8, 'B': 8, 'V': 8, 'Q': 8, 'Y': 7, 'N': 7, 'L': 7, 'P': 7, 'E': 6, 'G': 6, 'J': 5, 'Z': 5, 'T': 5, 'I': 5, 'K': 4, 'H': 4, 'F': 4, 'O': 3, 'S': 2, 'W': 1, 'D': 1})
Key length: 6
Pos 0: Counter({'A': 12, 'X': 12, 'O': 9, 'B': 9, 'T': 8, 'U': 7, 'K': 7, 'V': 7, 'Q': 7, 'Z': 6, 'M': 6, 'L': 6, 'G': 6, 'P': 6, 'Y': 5, 'E': 5, 'I': 4, 'N': 3, 'S': 3, 'C': 2, 'W': 2, 'R': 2, 'H': 2, 'F': 2, 'J': 1, 'D': 1})
Pos 1: Counter({'R': 16, 'Q': 13, 'L': 12, 'M': 9, 'J': 8, 'C': 8, 'N': 7, 'G': 7, 'A': 6, 'U': 6, 'Y': 5, 'E': 5, 'I': 5, 'W': 4, 'B': 4, 'V': 4, 'P': 4, 'F': 4, 'X': 3, 'O': 3, 'K': 2, 'H': 2, 'S': 2, 'T': 1})
Pos 2: Counter({'X': 19, 'B': 13, 'M': 13, 'P': 10, 'A': 8, 'L': 8, 'E': 7, 'K': 6, 'T': 6, 'I': 6, 'W': 5, 'Z': 5, 'H': 4, 'J': 3, 'V': 3, 'G': 3, 'O': 3, 'Q': 3, 'U': 2, 'Y': 2, 'N': 2, 'R': 2, 'S': 2, 'D': 2, 'F': 2, 'C': 1})
Pos 3: Counter({'R': 14, 'N': 12, 'F': 11, 'P': 10, 'A': 9, 'L': 7, 'H': 7, 'U': 6, 'C': 6, 'E': 6, 'I': 6, 'X': 6, 'J': 5, 'M': 5, 'B': 4, 'V': 4, 'Q': 4, 'Y': 3, 'S': 3, 'D': 3, 'Z': 2, 'K': 2, 'G': 2, 'W': 1, 'T': 1, 'O': 1})
Pos 4: Counter({'B': 13, 'Y': 9, 'Z': 8, 'K': 8, 'T': 7, 'M': 7, 'L': 7, 'X': 7, 'O': 6, 'A': 6, 'U': 6, 'I': 6, 'C': 5, 'E': 5, 'H': 5, 'G': 5, 'P': 5, 'V': 4, 'R': 4, 'F': 4, 'W': 3, 'D': 3, 'J': 2, 'N': 2, 'Q': 2, 'S': 1})
Pos 5: Counter({'P': 14, 'R': 13, 'A': 10, 'C': 8, 'M': 8, 'W': 7, 'Y': 7, 'V': 7, 'E': 6, 'F': 6, 'J': 5, 'N': 5, 'B': 5, 'L': 5, 'G': 5, 'U': 4, 'Q': 4, 'I': 4, 'X': 4, 'S': 4, 'H': 3, 'Z': 2, 'D': 2, 'K': 1, 'T': 1})
Key length: 7
Pos 0: Counter({'B': 8, 'R': 8, 'A': 7, 'U': 7, 'K': 6, 'I': 6, 'G': 6, 'P': 6, 'N': 5, 'M': 5, 'E': 5, 'L': 5, 'V': 5, 'X': 5, 'Q': 5, 'J': 4, 'Y': 4, 'T': 4, 'W': 3, 'O': 3, 'C': 3, 'F': 3, 'Z': 2, 'H': 2, 'D': 2, 'S': 1})
Pos 1: Counter({'X': 12, 'Q': 11, 'L': 9, 'F': 8, 'H': 7, 'K': 6, 'M': 6, 'P': 6, 'A': 5, 'U': 5, 'Y': 5, 'T': 5, 'G': 5, 'R': 5, 'Z': 4, 'B': 4, 'W': 3, 'N': 3, 'I': 3, 'J': 2, 'C': 2, 'E': 2, 'D': 1, 'O': 1})
Pos 2: Counter({'X': 10, 'P': 10, 'B': 8, 'E': 8, 'M': 7, 'R': 7, 'Y': 6, 'T': 6, 'J': 5, 'G': 5, 'L': 5, 'A': 4, 'C': 4, 'K': 4, 'Q': 4, 'O': 3, 'U': 3, 'N': 3, 'H': 3, 'S': 3, 'W': 2, 'Z': 2, 'I': 2, 'V': 2, 'D': 2, 'F': 2})
Pos 3: Counter({'X': 11, 'A': 9, 'B': 7, 'V': 7, 'P': 7, 'Y': 6, 'N': 6, 'L': 6, 'F': 6, 'R': 6, 'U': 5, 'M': 5, 'E': 5, 'G': 5, 'W': 4, 'J': 4, 'C': 4, 'Z': 4, 'K': 4, 'Q': 2, 'H': 2, 'I': 2, 'O': 2, 'D': 1})
Pos 4: Counter({'A': 12, 'R': 10, 'M': 8, 'P': 8, 'E': 7, 'L': 7, 'B': 6, 'O': 6, 'C': 5, 'N': 5, 'V': 5, 'W': 4, 'Y': 4, 'F': 4, 'J': 3, 'K': 3, 'T': 3, 'X': 3, 'H': 3, 'S': 3, 'I': 3, 'G': 3, 'Q': 2, 'U': 1, 'Z': 1, 'D': 1})
Pos 5: Counter({'B': 11, 'R': 8, 'M': 8, 'N': 7, 'Z': 7, 'S': 7, 'I': 7, 'A': 5, 'C': 5, 'V': 5, 'O': 5, 'E': 4, 'L': 4, 'H': 4, 'P': 4, 'Q': 4, 'J': 3, 'G': 3, 'X': 3, 'D': 3, 'F': 3, 'W': 2, 'U': 2, 'Y': 2, 'K': 2, 'T': 2})
Pos 6: Counter({'A': 9, 'M': 9, 'L': 9, 'U': 8, 'I': 8, 'P': 8, 'C': 7, 'X': 7, 'R': 7, 'V': 5, 'Q': 5, 'W': 4, 'Y': 4, 'T': 4, 'B': 4, 'J': 3, 'Z': 3, 'E': 3, 'F': 3, 'N': 2, 'H': 2, 'O': 2, 'K': 1, 'G': 1, 'S': 1, 'D': 1})
Key length: 8
Pos 0: Counter({'M': 13, 'L': 13, 'B': 10, 'I': 9, 'V': 8, 'P': 7, 'W': 6, 'Q': 6, 'E': 4, 'A': 4, 'C': 4, 'Z': 4, 'T': 4, 'N': 3, 'K': 3, 'U': 2, 'S': 2, 'X': 2, 'O': 1})
Pos 1: Counter({'N': 13, 'Q': 12, 'C': 10, 'M': 8, 'A': 8, 'R': 8, 'X': 7, 'W': 5, 'J': 5, 'B': 4, 'U': 4, 'V': 4, 'P': 4, 'F': 4, 'H': 3, 'E': 2, 'G': 1, 'D': 1, 'T': 1, 'O': 1})
Pos 2: Counter({'X': 21, 'A': 12, 'B': 8, 'H': 8, 'T': 7, 'M': 6, 'U': 6, 'P': 6, 'G': 5, 'W': 4, 'V': 4, 'K': 4, 'Y': 3, 'Z': 3, 'E': 2, 'L': 2, 'F': 2, 'I': 1, 'N': 1})
Pos 3: Counter({'R': 23, 'A': 12, 'U': 11, 'N': 11, 'F': 7, 'E': 5, 'Y': 5, 'Q': 5, 'G': 4, 'H': 3, 'V': 3, 'L': 3, 'B': 2, 'S': 2, 'C': 2, 'J': 2, 'T': 1, 'I': 1, 'Z': 1, 'P': 1, 'O': 1})
Pos 4: Counter({'B': 14, 'X': 9, 'A': 8, 'P': 8, 'F': 6, 'E': 6, 'Q': 6, 'O': 6, 'T': 6, 'D': 6, 'I': 5, 'K': 5, 'M': 4, 'L': 4, 'Z': 4, 'Y': 3, 'J': 2, 'C': 2, 'V': 1})
Pos 5: Counter({'P': 18, 'C': 10, 'L': 9, 'M': 8, 'J': 8, 'Y': 8, 'F': 8, 'B': 7, 'G': 7, 'R': 5, 'D': 3, 'Q': 3, 'E': 2, 'A': 2, 'S': 2, 'U': 1, 'I': 1, 'V': 1, 'Z': 1, 'K': 1})
Pos 6: Counter({'O': 11, 'Y': 10, 'G': 9, 'K': 9, 'Z': 8, 'R': 8, 'U': 7, 'X': 6, 'E': 5, 'S': 4, 'J': 4, 'T': 4, 'B': 3, 'H': 3, 'M': 3, 'N': 3, 'L': 2, 'A': 2, 'C': 2, 'I': 1, 'V': 1})
Pos 7: Counter({'I': 13, 'L': 12, 'E': 8, 'W': 7, 'R': 7, 'V': 7, 'M': 6, 'H': 6, 'X': 6, 'P': 5, 'S': 5, 'K': 4, 'J': 3, 'A': 3, 'O': 2, 'Y': 2, 'Z': 2, 'F': 2, 'G': 2, 'T': 1, 'D': 1, 'Q': 1})
'''

# Find the length of the key, by looking at coincidences
# turn chars in string into list of corresponding numbers
my_chars =[]
for char in my_string:
    my_chars.append(char)

for behind in range(4, 41):
    coincidences = 0
    for i in range(behind, len(my_chars)):
        if my_chars[i] == my_chars[i-behind]:
            coincidences += 1
    print(str(behind) + ' coincidences: ' + str(coincidences))

'''
4 coincidences: 32
5 coincidences: 26
6 coincidences: 31
7 coincidences: 25
8 coincidences: 55 *
9 coincidences: 36
10 coincidences: 38
11 coincidences: 34
12 coincidences: 33
13 coincidences: 36
14 coincidences: 30
15 coincidences: 28
16 coincidences: 51 *
17 coincidences: 39
18 coincidences: 23
19 coincidences: 31
20 coincidences: 33
21 coincidences: 30
22 coincidences: 26
23 coincidences: 33
24 coincidences: 43 *
25 coincidences: 36
26 coincidences: 34
27 coincidences: 29
28 coincidences: 36
29 coincidences: 27
30 coincidences: 31
31 coincidences: 36
32 coincidences: 41 *
33 coincidences: 33
34 coincidences: 30
35 coincidences: 38 ~
36 coincidences: 34
37 coincidences: 30
38 coincidences: 41 * please be a false positive!
39 coincidences: 27
40 coincidences: 39 *

Length 8

Pos 0 is shifted 7 or 8 (possibly 1) I
Pos 1 is shifted 9 (possibly 12) J
Pos 2 is shifted 19 (v.likely) T
Pos 3 is shifted 13 (v.likely) N
Pos 4 is shifted 23 (v.likely) X
Pos 5 is shifted 11 (v.likely, 24 next) L
Pos 6 is shifted 10 (possiblly 20, possibly 2 or 6) G
Pos 7 is shifted 4 (possibly 7) E

Key is IJTNXYGE
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

shift = {
    0: 8,
    1: 9,
    2: 19,
    3: 13,
    4: 23,
    5: 24,
    6: 6,
    7: 4
}

my_chars =[]
for char in my_string:
    my_chars.append(alphabet[char])

i = 0
shifted_chars = []
for char in my_chars:
    shifted_chars.append(rev_alphabet[(char - shift[i%8])%26])
    i += 1
print(''.join(str(x) for x in shifted_chars))
