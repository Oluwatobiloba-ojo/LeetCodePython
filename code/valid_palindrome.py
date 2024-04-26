def replaceEveryCharsToEmptyString(value):
    for char in value:
        if not char.isalpha():
            value = value.replace(char, "")
    return value


def isPalindrome(value: str):
    value = replaceEveryCharsToEmptyString(value)
    value = value.lower()
    return value[::-1] == value
