from base64 import b64encode as enc
from random import randint
from string import ascii_letters, printable, digits


def genRegexPattern(string):
    global symbol

    res = ""
    for i, x in enumerate(string):
        if (asd := randint(0, 4)) == 0:
            res += f"[{x}]"
        elif asd == 1:
            if i != len(string) - 1:
                res += f"[{x}](?={string[i+1]})"
            else:
                res += f"[{x}]"
        elif asd == 2:
            if i != 0:
                res += f"(?<={string[i-1]})[{x}]"
            else:
                res += f"[{x}]"
        elif asd == 3:
            if x in ascii_letters:
                res += f"[^\W\d{''.join([a for a in ascii_letters if a != x])}]"
            elif x in digits:
                res += f"[^\W\D{''.join([a for a in digits if a != x])}]"
            elif x in symbol:
                x = f"\{x}"
                res += f"[^\w\d{''.join([a for a in symbol if a != x])}]"
        elif asd == 4:
            res += f"([^\w\d{symbol}]|[{x}])"

    return res


flag = b"## REDACTED ##"

symbol = printable[62:-5].replace("\\", "")
symbol += "".join([f"\{x}" for x in symbol])
symbol += r"\r\t\n\\"

iteration = REDACTED # this should be a number, but its redacted so its fair for everyone
result = ""
for _ in range(iteration):
    temp = enc(flag).decode("ascii")
    result += genRegexPattern(temp)

open("chall.txt", "w").write(result)
