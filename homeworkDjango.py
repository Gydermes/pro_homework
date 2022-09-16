import re


def login(login_name: str):
    if not isinstance(login_name, str):
        raise TypeError()
    regex = "^[a-zA-Z0-9]+$"
    res = re.compile(regex)
    if 2 <= len(login_name) <= 10 and res.search(login_name) is not None:
        return login_name
    return "correct login"


res = login('2562*')
print(res)

import re


s = 'GfdfRb kRbrasd sadRbbr Rbr 24Rbbbrsasd'
res = re.findall(r'Rbr|Rbbr|Rbbbr', s)
if res:
    print(res)
else:
    print('None')


# import validate v
# def number_cart(cart:int):
#     if not isinstance(cart, int):
#         raise TypeError()
#     print(v.lengh(16).validate(cart))
#
#
# res = number_cart(1616161616161616)


import re


def mail(name):
    if re.findall(r'^[a-zA-Z0-9]+$', name):
        return name

    return "correct mail"


res = mail('Gydermes23')
print(res)
