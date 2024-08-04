from account import Account
from except_account import *
from income_cost import Income, Cost
import pprint
import getpass
from user import Authenticator


while True:
    n = int(input('Choose a number:\n1. Create user\n2. Log in\n3. Exit\n'))
    if n == 3:
        print('Goodbye...')
        break
    
    elif n == 1:
        while True:
            if Authenticator.check_username_exist():
                print("You've already have an account")
                break
            user1 = Authenticator()
            username = input('Username: ')
            password = input('Password: ')   
            print(x:=user1.add_user(username, password))
            if x == 'Password too short':
                for_continue = input('You want to continue to create user?(yes\\no) ')
                if for_continue.lower() == 'yes':
                    continue
            break

    elif n == 2:
        username = input('Username: ')
        password = getpass.getpass(prompt='Password:')
        user2 = Authenticator()
        print(x:=user2.login(username, password))
        if x == 'User logged in':
            while True:
                n = int(input('Choose a number:\n1. Create bank account\n2. Manage your account\
                              \n3. Change username and password\n4. Log out\n'))
                if n == 1:
                    while True:
                        try:
                            bank_name = input('Bank name: ')
                            balance = input('Balance: ')
                            account_number = input('Account number: ')
                            card_number = input('Card number: ')
                            account = Account(account_number)
                            print(account.add_account(bank_name, balance, card_number))
                            break
                        except BaseException as b:
                            print(b)
                        except Exception as e:
                            print(e)
                        for_continue = input('You want to continue to create account?(yes\\no) ')
                        if for_continue == 'no':
                            break
                elif n ==2:
                    account_number = input('In which account number you want to manage?\n')
                    check_account = ValidateAccountNumber(account_number)
                    while check_account.check_account_number():
                        n = int(input('Choose a number:\n1. Income\n2. Cost\
                                \n3. Show information\n4. Show list of transaction\n5. Back to main menu\n'))
                        # income
                        if n == 1:
                            while True:
                                try:
                                    income = Income(account_number)
                                    new_or_old = input('Is it a new income?(yes\\no) ')
                                    if new_or_old.lower() == 'yes':
                                        category = int(input('In which category is it?(Choose a number)\n1. Salary\
                                                            \n2. Interest\n3. Inheritance\n4. Etc\n'))
                                        if category not in [1, 2, 3, 4]:
                                            print('Enter valid number')
                                            continue
                                        new_income = input('What is it? ')
                                        frequent_activity = input('Is it a frequent activity?(yes\\no) ')
                                        amount_of_income = input('Amount of income: ')
                                        income.add(category, new_income, amount_of_income, frequent_activity)
                                        print(f'New income successfully aded')
                                        break
                                    else:
                                        print('Choose a number of options:')
                                        for i in income.old_incomes():
                                            print(i[0], '. ', i[1], sep='')
                                        old_income = int(input())
                                        if old_income >= len(income.old_incomes()):
                                            print('Out of range')
                                            continue
                                        amount_of_income = input('Amount of income: ')
                                        income.add_old_income(old_income, amount_of_income)
                                        print(f'Old income successfully aded')
                                        break
                                except BaseException as b:
                                    print(b)
                                except Exception as e:
                                    print(e)
                                for_continue = input('You want to continue to add income?(yes\\no) ')
                                if for_continue == 'no':
                                    break
                        # cost
                        elif n == 2:
                            while True:
                                try:
                                    cost = Cost(account_number)
                                    new_or_old = input('Is it a new cost?(yes\\no) ')
                                    if new_or_old.lower() == 'yes':
                                        category = int(input('In which category is it?(Choose a number)\n1. Clothing\
                                                            \n2. Food\n3. Car\n4. Etc\n'))
                                        if category not in [1, 2, 3, 4]:
                                            print('Enter valid number')
                                            continue
                                        new_cost = input('What is it? ')
                                        frequent_activity = input('Is it a frequent activity?(yes\\no) ')
                                        amount_of_cost = input('Amount of cost: ')
                                        cost.add(category, new_cost, amount_of_cost, frequent_activity)
                                        print('New Cost successfully aded')
                                        break
                                    else:
                                        print('Choose a number of options:')
                                        for i in cost.old_cost():
                                            print(i[0], '. ', i[1], sep='')
                                        old_cost = int(input())
                                        if old_cost >= len(cost.old_cost()):
                                            print('Out of range')
                                            continue
                                        amount_of_cost = input('Amount of cost: ')
                                        cost.add_old_cost(old_cost, amount_of_cost)
                                        print('Old cost successfully aded')
                                        break
                                except BaseException as b:
                                    print(b)
                                except Exception as e:
                                    print(e)
                                for_continue = input('You want to continue to add cost?(yes\\no) ')
                                if for_continue == 'no':
                                    break
                        elif n == 3:
                            account = Account(account_number)
                            print(account)
                        elif n == 4:
                            account = Account(account_number)
                            account.get_information()
                            list_of_transaction = account.transaction[1:-1].split(',')
                            pprint.pprint(list_of_transaction)
                        elif n == 5:
                            print('Main menu')
                            break
                        else:
                            print('Enter valid number')
                    else:
                        print('Wrong account number')
                elif n == 3:
                    new_username = input('New username: ')
                    new_password = input('New password: ')
                    print(user2.change_username(new_username, new_password))
                elif n == 4:
                    print('User loged out')
                    break
                else:
                    print('Type a correct number')
    else:
        print('Type a correct number')