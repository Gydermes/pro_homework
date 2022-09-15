import re


def login(login_name: str):
    if not isinstance(login_name, str):
        raise TypeError()
    regex = "^[a-zA-Z0-9]+$"
    pattern = re.compile(regex)
    if 2 <= len(login_name) <= 10 and pattern.search(login_name) is not None:
        print(login_name)
    else:
        print("correct login")


res = login('*(sds')

