if __name__ == "__main__":
    print('loop 1 :')
    print(''.join([f'{a}, ' for a in range(10)]))
    
    print('\n-------')

    print('loop 2 :')
    print(''.join([f'{a}, ' for a in range(0, 10, 2)]))
    
    print('\n-------')

    print('loop 3 :')
    print(''.join([f'{a}, ' for a in range(10, 0, -2)]))