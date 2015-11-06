# Brute Force a Caeser Cipher
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
# Open file and assign it to a string
my_file = open('ss835.txt', 'r')
my_string = my_file.read()
# Trim the '\n' from the end of the string
my_string = my_string[:len(my_string)-1]
my_file.close()

my_chars =[]

for char in my_string:
    my_chars.append(alphabet[char])

print(my_string + '\n')

for position in alphabet:
    add = alphabet[position] # start at 0 and up to 25
    new_chars = []
    for char in my_chars:
        new_chars.append(rev_alphabet[(char + add)%26])
    print('Shift ' + str(add) + ':')
    print(''.join(str(x) for x in new_chars))
    print()
