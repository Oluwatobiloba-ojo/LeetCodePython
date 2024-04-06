import math


def doubleCommaValue(value: str):
    return list(map(lambda x: int(math.pow(int(x), 2)), value.split(",")))


def main():
    value = input("Enter the value: ")
    print(doubleCommaValue(value))


main()
