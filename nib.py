import math

with open("nibbles.txt", 'r') as f:
    data = f.readlines()

j = []
clean = []

##Constellation Coordinates
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

##Constellation pairs
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

##Nibbles (4 bits)
nibbles = []

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

    nibbles.append(const[y][x])

##Ascii value in Bytes
ascii2 = []

for i in range(0, len(nibbles), 2):
    ascii2.append(nibbles[i]+nibbles[i+1])

ascii3 = []
##Byte to Ascii int value
for i in range(0, len(ascii2)):
    ascii3.append(int(ascii2[i], 2))

##Decoded message
message = ''

for i in ascii3:
    message = message + chr(i)

##for i in range(0, len(ascii2)):
##    print("{0:2} {1} {2}".format(str(i+1), chr(ascii3[i]), str(ascii2[i])))

count = 0
for i in range(0, len(clean)):
    print("({}) decodes as {}".format(clean[i], nibbles[i]))
    if ((i+1)%2) == 0:
        print('together, {} gives "{}"'.format(ascii2[count], chr(ascii3[count])))
        count += 1

print("\nfinal decoded message: \n" + message)
