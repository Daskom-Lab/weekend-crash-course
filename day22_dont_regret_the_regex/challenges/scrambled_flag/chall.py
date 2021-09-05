# Solution:
# REDACTED

from string import ascii_lowercase, printable as pri, digits
from random import randint, choice


def getRandomExcept(randomset, char):
    while (ret := choice([x for x in randomset])) == char:
        continue

    return ret


flag = r"## REDACTED ##"

printable = pri[:-6]
garbageNums = 1000

scrambled = ""
for x in flag:
    if randint(0, 1):
        for _ in range(randint(1, garbageNums)):
            if randint(0, 1):
                scrambled += f"{getRandomExcept(printable, '-')}-"
            else:
                scrambled += f"+{getRandomExcept(printable, '+')}"

            scrambled += getRandomExcept(digits, x)

    if x == "i":
        scrambled += f"{getRandomExcept(ascii_lowercase, x)}!"
    elif x == "f":
        scrambled += f"{getRandomExcept(ascii_lowercase, x)}%"
    elif x == "g":
        scrambled += f"{getRandomExcept(ascii_lowercase, x)}$"
    elif x in digits:
        scrambled += f"{x}X"
    else:
        scrambled += x

    if randint(0, 1):
        for _ in range(randint(1, garbageNums)):
            if randint(0, 1):
                scrambled += f"{getRandomExcept(printable, '-')}-"
            else:
                scrambled += f"+{getRandomExcept(printable, '+')}"

            scrambled += getRandomExcept(digits, x)

open("chall.txt", "w").write(scrambled)
