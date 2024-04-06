from collections import Counter

Counter()


def validateLength(first, second):
    return len(first) == len(second)


ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def arrangeWords(first: str, second: str, arrange_first: str, arrange_second: str, letter: str):
    arrange_first += "".join(map(str, [word for word in first if word == letter]))
    arrange_second += "".join(map(str, [word2 for word2 in second if word2 == letter]))
    return [arrange_first, arrange_second]


def isAnagram(first: str, second: str) -> bool:
    arrange_first = ""
    arrange_second = ""
    count = 0
    if not validateLength(first, second):
        return False
    while len(arrange_first) != len(first) and count != 26:
        arrange_first, arrange_second = arrangeWords(first, second, arrange_first, arrange_second, ALPHABET[count])
        count += 1
        if arrange_first != arrange_second:
            return False
    return True
