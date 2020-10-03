if __name__ == "__main__":
    while(x := input('Y/N: ') == 'Y'):
        print('yess')
    else:
        print('nooo')

    for i in range(x := int(input('n = '))):
        print(i, end='')
        if i := i + 1 < len(range(x)):
            print(', ', end='')
