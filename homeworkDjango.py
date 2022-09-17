import re

s = 'GfdfRb kRbrasd sadRbbr Rbr 24Rbbbrsasd'
res = re.findall(r'Rbr|Rbbr|Rbbbr', s)
if res:
    print(res)
else:
    print('None')


def cart(number):
    if re.findall(r'^[\d]{16}$', number):

        return 'card number entered correctly'

    return "wrong cart"


res = cart('1234567890123456')
print(res)


def mail(name):
    if re.findall(r'^[a-zA-Z\d_-]+@[a-zA-Z\d]+.[a-z]+$', name):

        return name

    return "wrong mail"


res = mail('fmk26hbgh@gmail943.com')
print(res)


def login(login_name: str):
    if not isinstance(login_name, str):
        raise TypeError()
    res = re.compile(r'^[a-zA-Z\d]+$')
    if 2 <= len(login_name) <= 10 and res.search(login_name) is not None:
        return login_name
    return "wrong login"


result = login('23eSSasz')
print(result)

