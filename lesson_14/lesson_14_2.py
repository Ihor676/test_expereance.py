class LoginError(Exception):
    msg = 'Неверный логин!'

    def __init__(self, value=None):
        if value is not None:
            self.msg = value
    def __str__(self):
        return self.msg

def f_login(login):
    pass_login = 'ihor.i147'

    try:
        if login != pass_login:
            raise LoginError('Неверный логин!')
    except LoginError as error:
        print(error.__str__())

name = input('Введите логин(правильный логин ihor.i147):')
f_login(name)


