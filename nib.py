import math

with open("nibbles.txt", 'r') as f:
    data = f.readlines()

j = []
clean = []
const = [['0000','0100','1100','1000'],
         ['0001','0101','1101','1001'],
         ['0011','0111','1111','1011'],
         ['0010','0110','1110','1010']]

for i in data:
    j.append(i[-15:-3])

for p in j:
    p = p.strip()
    p = p.strip('(')
    clean.append(p)

pairs = []


for c in clean:
    pairs.append(c.split(', '))

for i in range(0, len(pairs)):
    for x in range(0, 2):
        pairs[i][x] = float(pairs[i][x])
        if pairs[i][x] > 2:
            pairs[i][x] = 3
        elif pairs[i][x] < 2 and pairs[i][x] > 0:
            pairs[i][x] = 1
        elif pairs[i][x] > -2 and pairs[i][x] < 0:
            pairs[i][x] = -1
        elif pairs[i][x] < -2:
            pairs[i][x] = -3
        else:
            pairs[i][x] = '[NP]'

##Actually nibbles
ascii = []

for i in range(0, len(pairs)):
    if pairs[i][0] == -3:
        x = 0
    elif pairs[i][0] == -1:
        x = 1
    elif pairs[i][0] == 1:
        x = 2
    elif pairs[i][0] == 3:
        x = 3

    if pairs[i][1] == -3:
        y = 3
    elif pairs[i][1] == -1:
        y = 2
    elif pairs[i][1] == 1:
        y = 1
    elif pairs[i][1] == 3:
        y = 0

    ascii.append(const[y][x])

##Ascii value in Bytes
ascii2 = []

for i in range(0, len(ascii), 2):
    ascii2.append(ascii[i]+ascii[i+1])

for i in range(0, len(ascii2)):
    ascii2[i] = int(ascii2[i], 2)

##Decoded message
message = ''

for i in ascii2:
    message = message + chr(i)

