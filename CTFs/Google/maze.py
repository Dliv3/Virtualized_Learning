import sys

flag = [0x83,0x01,0xaf,0x49,0xad,0xc1,0x0f,0x8b,0xe1]
for i in range(len(flag)):
    for j in range(256):
        if j+flag[i] == 0x100:
            print i+1,hex(flag[i]),j,
            r = j / 16
            c = j % 16
            print "(" + str(r) + "," + str(c) + ")"

list1 = [
    1, 0, 1, 0, 0, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 0, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0, 0, 0,
    1, 0, 1, 0, 1, 0, 1, 0,
]

list2 = [0xCC, 0xB0, 0xE7, 0x7B, 0xBC, 0xC0, 0xEE, 0x3A, 0xFC, 0x73,
         0x81, 0xD0, 0x7A, 0x69, 0x84, 0xE2, 0x48, 0xE3, 0xD7, 0x59,
         0x11, 0x6B, 0xF1, 0xB3, 0x86, 0x0B, 0x89, 0xC5, 0xBF, 0x53,
         0x65, 0x65, 0xF0, 0xEF, 0x6A, 0xBF, 0x08, 0x78, 0xC4, 0x2C,
         0x99, 0x35, 0x3C, 0x6C, 0xDC, 0xE0, 0xC8, 0x99, 0xC8, 0x3B,
         0xEF, 0x29, 0x97, 0x0B, 0xB3, 0x8B, 0xCC, 0x9D, 0xFC, 0x05,
         0x1B, 0x67, 0xB5, 0xAD, 0x15, 0xC1, 0x08, 0xD0, 0x45, 0x45,
         0x26, 0x43, 0x45, 0x6D, 0xF4, 0xEF, 0xBB, 0x49, 0x06, 0xCA,
         0x73, 0x6B, 0xBC, 0xE9, 0x50, 0x97, 0x05, 0xE5, 0x97, 0xD3,
         0xB5, 0x47, 0x2B, 0xAD, 0x25, 0x8B, 0xAE, 0xAF, 0x41, 0xE5,
         0xD8, 0x14, 0xF4, 0x83, 0xE6, 0xF0, 0xC0, 0x98, 0x0A, 0xAC,
         0xA1, 0x95, 0xF5, 0xB5, 0xD3, 0x53, 0xF0, 0x97, 0xEF, 0x9D,
         0xD4, 0x3B, 0x3B, 0x0B, 0xE7, 0x17, 0x07, 0x1F, 0x6C, 0xF1,
         0x1E, 0x44, 0x92, 0xB2, 0x57, 0x07, 0xB7, 0x36, 0x8F, 0x53,
         0xC9, 0xEA, 0x10, 0x90, 0x62, 0xDF, 0x1D, 0x07, 0xB3, 0x71,
         0x53, 0x61, 0x1A, 0x2B, 0x78, 0xBF, 0xC1, 0xB5, 0xC6, 0x3B,
         0xEA, 0x2B, 0x44, 0x17, 0xA0, 0x84, 0xCA, 0x8F, 0xB7, 0x3B,
         0x38, 0x2F, 0xE8, 0x73, 0x84, 0xAD, 0x44, 0xEF, 0xF8, 0xAD,
         0x8C, 0x1F, 0xEA, 0x7F, 0xCD, 0xC5, 0xB3, 0x49, 0x05, 0x03,
         0x95, 0xA7, 0x44, 0xB5, 0x91, 0x69, 0xF8, 0x95, 0x6C, 0xE5,
         0x87, 0x53, 0x4E, 0x47, 0x92, 0xBE, 0x80, 0xD0, 0x80, 0x1D,
         0xAD, 0xF1, 0x3D, 0xE3, 0xDF, 0x35, 0x61, 0xF1, 0xE7, 0x0D,
         0x71, 0xC5, 0x02, 0x4F, 0x20, 0x5E, 0xA2, 0x8B, 0xC4, 0x61,
         0x32, 0x0F, 0xA8, 0xBE, 0x7E, 0x29, 0xD1, 0x6D, 0x2A, 0xD9,
         0x55, 0x47, 0x07, 0x83, 0xEA, 0x2B, 0x79, 0x95, 0x4F, 0x3D,
         0xA3, 0x11, 0xDD, 0xC1, 0x1D, 0x89]

map = [0] * len(list2)

for i in range(len(list2)):
    if list1[list2[i]*2]:
        map[i] = '\033[1;37;47m \033[0m'
    else:
        map[i] = ' '

for i in range(256):
    if i / 16 == 7 and  i % 16 == 13:
        sys.stdout.write('1')
    elif i == 17:
        sys.stdout.write('\033[1;32;42m \033[0m')
    elif i / 16 == 15 and i % 16 == 15:
        sys.stdout.write('2')
    elif i/16 == 5 and i%16 == 1:
        sys.stdout.write('3')
    elif i/16 == 11 and i%16 == 7:
        sys.stdout.write('4')
    elif i/16 == 5 and i%16 == 3:
        sys.stdout.write('5')
    elif i/16 == 3 and i%16 == 15:
        sys.stdout.write('6')
    elif i/16 == 15 and i%16 == 1:
        sys.stdout.write('7')
    elif i/16 == 7 and i%16 == 5:
        sys.stdout.write('8')
    elif i/16 == 1 and i%16 == 15:
        sys.stdout.write('9')
    else:
        if i % 16 == 0 and i != 0:
            print '\033[1;37;47m \033[0m'
            sys.stdout.write(map[i])
        else:
            sys.stdout.write(map[i])

print '\033[1;37;47m \033[0m'

for i in range(17):
    sys.stdout.write('\033[1;37;47m \033[0m')

print ""