from os import listdir, stat
from os.path import isfile, join

if __name__ == "__main__":
    onlyfiles = [f for f in listdir(
        'challenge/') if isfile(join('challenge/', f))]

    onlypngs = [f for f in onlyfiles if f.split('.')[-1] == 'png'
                and f.split('.')[0] != 'batman'
                and f.split('.')[0] != 'nightwing']
    onlypngs.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    batman = stat('challenge/batman.png').st_size

    binary = ''
    for png in onlypngs:
        if stat(f'challenge/{png}').st_size == batman:
            binary += '1'
        else:
            binary += '0'

    print(bytes.fromhex(hex(int(binary, 2))[2:]).decode())