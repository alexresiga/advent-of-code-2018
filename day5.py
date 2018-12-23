def react(a, b):
    return a.lower() == b.lower() and abs(ord(a) - ord(b)) == 32


def remove_unit(word, letter: str):
    return word.replace(letter, "").replace(letter.upper(), "")


def full_react(word):
    ii = 0
    while ii < len(word) - 1:
        if react(word[ii], word[ii + 1]):
            word = word.replace(word[ii:ii + 2], "")
            if ii > 0:
                ii -= 1
        else:
            ii += 1
    return word


with open('data.in', 'r') as f:
    polymer = f.readline()
    units = {}
    letters = set()
    for l in polymer.lower():
        letters.add(l)
    for i in range(97, 123):
        units[chr(i)] = 0
    for l in letters:
        tmp = polymer
        units[l] = len(full_react(remove_unit(tmp, l)))
    print(sorted([x for x in units.items() if x[1] != 0], key=lambda k: k[1]))
