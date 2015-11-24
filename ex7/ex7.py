from collections import Counter

# Open file and assign it to a string
my_file = open('ss835.txt', 'r')
my_string = my_file.read()
# Trim the '\n' from the end of the string
my_string = my_string[:len(my_string)-1]
my_file.close()

# frequency analysis
data = Counter(my_string)
print(data)

'''
Result:

Counter({'G': 156, 'M': 90, 'B': 59, 'U': 56, 'K': 54, 'Z': 53, 'L': 47, 'P': 45,
'|': 42, 'I': 36, 'S': 35, 'A': 24, 'H': 21, 'F': 18, 'R': 16, 'O': 16, 'J': 13,
'Q': 13, 'X': 13, 'W': 11, 'T': 8, 'D': 7, 'C': 4, 'V': 2, 'E': 1})

'G' is clearly '|' and 'M' is likely to be 'E'

Step 1: replace G with ' '
Step 2: Look for THE (M is probaly E)
    UBM repeats a lot, probably THE.
Step 3: look for Repeating Letter
    2x FF
    1x II
    2x KK
    3x LL : most common, possibly ll... inconclusive
    1x MM
    2x OO
    1x VV
Step 4: get replacing and look for words, start with U, B & M for 'the'

    Commonly found:
    he|: her or hes?
    Lhe: must be she assuming 'the' was correct; L = s
        therefore | is probably r
            found 'threshers', sounds good so far!
    sI Zs tI De: 4 2 letter words together... weird.
    theJ: they, them, thee, then...
    arJs: J probably m
    several Zt and Zs: Z probably i
        nope found a 'thit': Z = a
    Rrame: R probably f
    faAts: A probably c
    PKcessaKt: most likely incessant: P = i, K = n,
    anS : S = d
    seFarated: F = p
    preCented: C = v
    chanQinQ: Q = g
    fOapping: O = l
    tI, If: I = o
    Homen, Hhich: H = w
    conscioXsness: X = u
    clung to them liTe dull flames: T = k
    independentlW: W = y
    Donnet, emDrowned, Dy: D = B
    Euivering: E = q
    iVV: V = z

Done!
'''
dictionary = {
    'G':'|',
    'M': 'E',
    'U': 'T',
    'B': 'H',
    'L': 'S',
    '|': 'R',
    'J': 'M',
    'Z': 'A',
    'R': 'F',
    'A': 'C',
    'P': 'I',
    'K': 'N',
    'S': 'D',
    'F': 'P',
    'C': 'V',
    'Q': 'G',
    'O': 'L',
    'I': 'O',
    'H': 'W',
    'X': 'U',
    'T': 'K',
    'W': 'Y',
    'D': 'B',
    'E': 'Q',
    'V': 'Z'
}

decrypted = []
for char in my_string:
    decrypted.append(dictionary[char]);
print(''.join(str(x) for x in decrypted))
