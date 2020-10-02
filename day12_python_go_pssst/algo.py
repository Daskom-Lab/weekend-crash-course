def solver(num):
    counter = 0
    for x in str(num):
        try:
            counter += (1 if num%int(x)==0 else 0)
        except :
            continue
    return counter

if __name__ == "__main__":
    cases = int(input())
    for i in range(cases):
        case = int(input())
        print(solver(case))