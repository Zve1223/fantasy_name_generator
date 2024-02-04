from random import randint, random

vowels = ['a', 'o', 'e', 'i', 'u', 'oo', 'ou', 'ee', 'au']
consonants = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
              'sh', 'ch', 'ss', 'zh', 'sch', 'ck', 'ph', 'th', 'gh', 'shch']


def get_random_number(start: float, stop: float, centering: float) -> float:
    return stop - (random() * (stop - start) ** centering) ** (1.0 / centering)


def get_random_letter(letters: list[str], centering: float) -> str:
    return letters[round(get_random_number(0, len(letters) - 1, centering))]


def get_random_syllable_count(centering: float) -> int:
    count = 3
    if randint(SHORT := 0, 1) == SHORT:
        count -= round(get_random_number(0.0, 2.0, centering))
    else:
        count += round(get_random_number(0.0, 7.0, centering))
    return count


def get_random_name() -> str:
    name = ''
    for n in range(get_random_syllable_count(4.0)):
        part = []

        if randint(DO_NOT_ADD_CONSONANT := 0, 9) != DO_NOT_ADD_CONSONANT:
            part.append(get_random_letter(consonants, 2.0))

        if randint(ADD_Y := 0, 7) == ADD_Y:
            part.append('y')

        part.append(get_random_letter(vowels, 4.0))

        if randint(ADD_CONSONANT := 0, 9) == ADD_CONSONANT:
            part.append(get_random_letter(consonants, 1.0))

        if randint(REVERSE := 0, 19) == REVERSE:
            part = part[::-1]

        name += ''.join(part)

    if randint(ADD_LAST_CONSONANT := 0, 19) == ADD_LAST_CONSONANT:
        name += get_random_letter(consonants, 4.0)

    return name.capitalize()
