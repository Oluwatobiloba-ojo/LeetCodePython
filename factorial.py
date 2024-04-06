import re
from enum import Enum


# def factorial(num):
#     if num == 0:
#         return 1
#     print(num)
#     return num * factorial(num - 1)
#
#
# print(factorial(5))


def validateEmail(email: str):
    email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,7}\b'
    if re.match(email_format, email):
        return True
    else:
        return False


user_email = "oluwapo@gmail.com"
print(validateEmail(user_email))
