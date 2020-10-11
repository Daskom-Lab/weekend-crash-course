import binascii

# Real Code
print('Daskom1337')

# Obfuscated code (hex mode)
print(binascii.hexlify(b'Daskom1337')) # -> 4461736b6f6d31333337
print(bytearray.fromhex('4461736b6f6d31333337'))

# Obfuscated code (string -> ascii -> hex)
print(''.join([hex(ord(x)) for x in 'Daskom1337'])) # -> 0x440x610x730x6b0x6f0x6d0x310x330x330x37
print(''.join([chr(int(f'0x{x}', 0)) for x in '0x440x610x730x6b0x6f0x6d0x310x330x330x37'.split('0x')[1:]]))

# Obfuscated code (branching)
print((j:='D' if (i:='a' if (h:='s' if (g:='k' if (f:='o' if (e:='m' if (d:='1' if (c:='3' if (b:='3' if (a:='7')=='7' else 'L')=='3' else 'O')=='3' else 'L')=='1' else 'O')=='m' else 'L')=='o' else 'O')=='k' else 'L')=='s' else 'O')=='a' else 'L')+i+h+g+f+e+d+c+b+a)

# Long Obfuscated code (branching)
j='D';i='a';h='s';g='k';f='o';e='m';d='1';c='3';b='3';a='7'
if a=='7':
    if b=='3':
        if c=='3':
            if d=='1':
                if e=='m':
                    if f=='o':
                        if g=='k':
                            if h=='s':
                                if i=='a':
                                    if j=='D':
                                        print(j+i+h+g+f+e+d+c+b+a)
                                    else:
                                        print('L')
                                else:
                                    print('O')
                            else:
                                print('L')
                        else:
                            print('O')
                    else:
                        print('L')
                else:
                    print('O')
            else:
                print('L')
        else:
            print('O')
    else:
        print('L')  
else:
    print('O')

# Obfuscated code (looping)
print(''.join([chr(i).upper() for i in range(ord('a'),ord('z'))][3:4]+[chr(i) for i in range(ord('a'),ord('z'))][0:1]+[chr(i) for i in range(ord('a'),ord('z'))][18:19]+[chr(i) for i in range(ord('a'),ord('z'))][10:11]+[chr(i) for i in range(ord('a'),ord('z'))][14:15]+[chr(i) for i in range(ord('a'),ord('z'))][12:13]+[str(i) for i in range(10)][1:2]+[str(i) for i in range(10)][3:4]+[str(i) for i in range(10)][3:4]+[str(i) for i in range(10)][7:8]))

# Long Obfuscated code (looping)
print(''.join([chr(i).upper() for i in range(ord('a'),ord('z'))][3:4]
            + [chr(i) for i in range(ord('a'),ord('z'))][0:1]
            + [chr(i) for i in range(ord('a'),ord('z'))][18:19]
            + [chr(i) for i in range(ord('a'),ord('z'))][10:11]
            + [chr(i) for i in range(ord('a'),ord('z'))][14:15]
            + [chr(i) for i in range(ord('a'),ord('z'))][12:13]
            + [str(i) for i in range(10)][1:2]
            + [str(i) for i in range(10)][3:4]
            + [str(i) for i in range(10)][3:4]
            + [str(i) for i in range(10)][7:8]
))