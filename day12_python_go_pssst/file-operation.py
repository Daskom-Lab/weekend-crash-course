if __name__ == "__main__":
    with open('test.txt', 'r') as f:
        print(f.read())

    print('-------')

    with open('test.txt', 'a') as f:
        print(f.write('\nTambahan: Daskom juga 1337'))

    print('-------')

    with open('bear.jpeg', 'rb') as f:
        print(''.join([f'{x}' + (' ' if c%2 != 0 else '')  for c, x in enumerate(f.read().hex()[:24])]))

    print('-------')

    open('cuman_buat.txt', 'x')