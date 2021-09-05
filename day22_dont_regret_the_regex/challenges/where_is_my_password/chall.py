# Solution:
# REDACTED

import random

passs = ""
isExist = False
garbageNums = 5000
randomPlacement = random.randint(garbageNums / 4, garbageNums * 3 // 4)
for x in range(garbageNums):
    if (asd := random.randint(1, 100)) == 25 and isExist:
        continue

    if asd == 25:
        isExist = True

    if x == randomPlacement and not isExist:
        isExist = True
        asd = 25

    passs += "-".join([f"{random.randint(0,9)}" for _ in range(asd)]) + ";"

open("chall.txt", "w").write(passs)
