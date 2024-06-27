class User:
    
    users = {}
    counter =1
    def __init__(self) -> None:
        pass

    def add_user(self):

        username = input('Username:')
        self.username = self.check_username(username)
        if self.username == 0:
            return 
        
        phone_number = input('Phone_number:')
        self.phone_number = phone_number
        
        password = input('Password:')
        self.__password = self.check_password(password)
        if self.__password == 1:
            return 

        self.users.update({self.username : [self.counter, self.phone_number, self.__password]})
        self.counter +=1
        print(self.users)
    

    def check_password(self, password):
        if password == None or len(password) < 4:
            print('Password incorrected')
            return 1
        else:
            return password

    def check_username(self, username):
        if username == '' or username in self.users.keys():
            print('The Username already exist')
            return 0
        else:
            return username

            
    
    def change_username_and_phone_number(self, username, password):
        new_username = input('New username: ')
        new_username = self.check_username(new_username)
        if new_username == 0:
            return
        self.username = new_username
        id = self.users[username][0]
        del self.users[username]
        new_phone_number = input('New phone number: ')
        self.users.update({new_username: [id, new_phone_number, password]})
        print('Username and phone number successfully changed')
    
    def change_password(self, username):
        new_password = input('New password: ')
        new_password = self.check_password(new_password)
        if new_password == 1:
            return
        repeat_password = input('Repeat your password: ')
        if repeat_password != new_password:
            print('Password and Repeat password doesnt match')
            return
        self.__password = new_password
        self.users[username][2] = self.__password
        print('Password successfully changed')



    
    def __str__(self) -> str:
        return f"'Username: '{self.username}\n'Id: '{self.users[self.username][0]}\n'Phone number: '{self.users[self.username][1]}"





while True:
    n = int(input('Choose a number:\n0. Exit\n1. Create user\n2. Managing your user\n'))
    if n == 0:
        print('Goodbye...')
        break
    
    elif n == 1:
        user1 = User()
        user1.add_user()    

    elif n == 2:
        username = input('Username:')
        if username not in user1.users.keys():
            print('Username not exist...')
        else:
            password = input('Password:')
            if user1.users[username][2] != password:
                print('Incorrect password')
            else:
                while True:
                    q = int(input('Choose a number:\n1. Display information\n2. Edit username and phone number\n3. Edit password\n4. Back to menu\n'))
                    if q == 1:
                        print(user1)
                    elif q == 2:
                        user1.change_username_and_phone_number(username,password)
                    elif q == 3:
                        password = input('Password:')
                        if user1.users[username][2] != password:
                            print('Incorrect password')
                        else:
                            user1.change_password(username)
                    elif q == 4:
                        break
    else:
        print('Type a correct number')

