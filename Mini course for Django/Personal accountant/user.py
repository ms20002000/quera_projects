from except_user import *
import uuid
import hashlib
import os.path
import csv

class Authenticator:

    def add_user(self, username, password):
            self.username = username
            check_pass = PasswordTooShort(password= password)
            if check_pass.password_check():
                self.password_hash = self.hashpassword(password)
                self.save_user()
                return f'User Successfully created'
            else:
                return f'Password too short'
            
    
    def save_user(self):
        if not os.path.exists('Uer.csv'):
            with open('User.csv', 'w', newline='') as cs:
                w = csv.writer(cs)
                w.writerow(['username', 'password'])
                w.writerow([self.username, self.password_hash])
        else:
            with open('Account.csv', 'a', newline='') as cs:
                    w = csv.writer(cs)
                    w.writerow([self.username, self.password_hash])


    def login(self, username, password):
        check_user = InvalidUsername(username)
        if check_user.check_username():
            self.password_hash = self.hashpassword(password)
            check_pass = InvalidPassword(username=username, password= self.password_hash)
            if check_pass.check_password():
                return f'User logged in'
            else:
                return f'Password invalid'
        else:
            return f'Username {username} is invalid'
        
    def change_username(self, username, password):
        self.username = username
        check_pass = PasswordTooShort(password= password)
        if check_pass.password_check():
            self.password_hash = self.hashpassword(password)
            with open('User.csv', 'w', newline='') as cs:
                w = csv.writer(cs)
                w.writerow(['username', 'password'])
                w.writerow([self.username, self.password_hash])
            return f'User Successfully changed'
        else:
            return f'Password too short'
        
    
    @classmethod
    def check_username_exist(cls):
        if not os.path.exists('User.csv'):
            return False
        else:
            with open('User.csv', 'r', newline='') as cs:
                r = csv.DictReader(cs)
                for i in r:
                    if len(i['username']) != 0:
                        return True
                return False

    @staticmethod
    def hashpassword(password):
        sha = hashlib.sha256()
        sha.update(password.encode('ASCII'))
        password_hash = sha.hexdigest()
        return password_hash
