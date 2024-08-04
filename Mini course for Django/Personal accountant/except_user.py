import csv

class AuthException:
    def __init__(self, username= None, password ='') -> None:
        self.username = username
        self.password = password

        

class PasswordTooShort(AuthException):
    def __init__(self, username=None, password='') -> None:
        super().__init__(username, password) 

    def password_check(self):
        if len(self.password) < 4:
            return False
        return True
    
class InvalidUsername(AuthException):
    def __init__(self, username=None, password='') -> None:
        super().__init__(username, password)

    def check_username(self):
        with open('User.csv', 'r', newline='') as cs:
            r = csv.DictReader(cs)
            for i in r:
                if i['username'] == self.username:
                    return True
            return False


class InvalidPassword(AuthException):
    def __init__(self, username=None, password='') -> None:
        super().__init__(username, password)

    def check_password(self):
        with open('User.csv', 'r', newline='') as cs:
            r = csv.DictReader(cs)
            for i in r:
                if i['password'] == self.password:
                    return True
            return False