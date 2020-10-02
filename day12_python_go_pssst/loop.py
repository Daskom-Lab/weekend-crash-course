if __name__ == "__main__":
    print('loop 1 :')
    for x in range(10):
        print(x, end=', ')
    
    print('\n-------')

    print('loop 2 :')
    for x in range(0, 10, 2):
        print(x, end=', ')
    
    print('\n-------')

    print('loop 3 :')
    for x in range(10, 0, -2):
        print(x, end=', ')
    
    print('\n-------')

    print('loop 4 :')
    i = 0
    while(i < 10):
        print(f'{i}', end=', ')
        i += 1