from itertools import accumulate
from bisect import bisect
from random import randint, randrange, choice

# Sauce: http://www.unicode.org/charts/PDF/U1F300.pdf
EMOJI_RANGES_UNICODE = {
    6: [
        ("\U0001F300", "\U0001F320"),
        ("\U0001F330", "\U0001F335"),
        ("\U0001F337", "\U0001F37C"),
        ("\U0001F380", "\U0001F393"),
        ("\U0001F3A0", "\U0001F3C4"),
        ("\U0001F3C6", "\U0001F3CA"),
        ("\U0001F3E0", "\U0001F3F0"),
        ("\U0001F400", "\U0001F43E"),
        ("\U0001F440",),
        ("\U0001F442", "\U0001F4F7"),
        ("\U0001F4F9", "\U0001F4FC"),
        ("\U0001F500", "\U0001F53C"),
        ("\U0001F540", "\U0001F543"),
        ("\U0001F550", "\U0001F567"),
        ("\U0001F5FB", "\U0001F5FF"),
    ]
}


def random_emoji(unicode_version=6):
    if unicode_version in EMOJI_RANGES_UNICODE:
        emoji_ranges = EMOJI_RANGES_UNICODE[unicode_version]
    else:
        emoji_ranges = EMOJI_RANGES_UNICODE[-1]

    # Weighted distribution
    count = [ord(r[-1]) - ord(r[0]) + 1 for r in emoji_ranges]
    weight_distr = list(accumulate(count))

    # Get one point in the multiple ranges
    point = randrange(weight_distr[-1])

    # Select the correct range
    emoji_range_idx = bisect(weight_distr, point)
    emoji_range = emoji_ranges[emoji_range_idx]

    # Calculate the index in the selected range
    point_in_range = point
    if emoji_range_idx != 0:
        point_in_range = point - weight_distr[emoji_range_idx - 1]

    return chr(ord(emoji_range[0]) + point_in_range)


# real_answer = "## REDACTED ##"
fake_answer = "## REDACTED ##"

garbageNums = 1000

temp = ""
for x in fake_answer:
    if randint(0, 1):
        temp += "".join([random_emoji() for _ in range(randint(1, garbageNums))])
        temp += "".join(
            [
                choice(
                    [
                        '"',
                        "#",
                        "$",
                        "%",
                        "&",
                        "\\",
                        "'",
                        "(",
                        ")",
                        "*",
                        "+",
                        ",",
                        "-",
                        ".",
                        "/",
                        ":",
                        ";",
                        "<",
                        "=",
                        ">",
                        "?",
                        "@",
                        "[",
                        "^",
                        "`",
                        "~",
                    ]
                )
                for _ in range(randint(1, garbageNums))
            ]
        )
        temp += "".join(
            [
                choice(["1", "2", "3", "5", "6", "7", "8", "9"])
                for _ in range(randint(1, garbageNums))
            ]
        )

    temp += x

    if randint(0, 1):
        temp += "".join([random_emoji() for _ in range(randint(1, garbageNums))])
        temp += "".join(
            [
                choice(
                    [
                        '"',
                        "#",
                        "$",
                        "%",
                        "&",
                        "\\",
                        "'",
                        "(",
                        ")",
                        "*",
                        "+",
                        ",",
                        "-",
                        ".",
                        "/",
                        ":",
                        ";",
                        "<",
                        "=",
                        ">",
                        "?",
                        "@",
                        "[",
                        "^",
                        "`",
                        "~",
                    ]
                )
                for _ in range(randint(1, garbageNums))
            ]
        )
        temp += "".join(
            [
                choice(["1", "2", "3", "5", "6", "7", "8", "9"])
                for _ in range(randint(1, garbageNums))
            ]
        )

    if x == "}":
        temp += "Never_gonna_give_you_up_Never_gonna_let_you_down_Never_gonna_run_around_and_desert_you_Never_gonna_make_you_cry_Never_gonna_say_goodbye_Never_gonna_tell_a_lie_and_hurt_you_We've_known_each_other_for_so_long_Your_heart's_been_aching_but_you're_too_shy_to_say_it_Inside_we_both_know_what's_been_going_on_We_know_the_game_and_we're_gonna_play_it_And_if_you_ask_me_how_I'm_feeling_Don't_tell_me_you're_too_blind_to_see"

open("chall.txt", "w").write(temp)
