import csv
import os.path
from except_account import *
import pandas as pd

class Account():
    def __init__(self, account_number: str) -> None:
        self.account_number = account_number
        
        
    def add_account(self, bank_name: str, balance: str, card_number:str):
        self.bank_name = bank_name
        self.balance = balance
        self.card_number = card_number
        self.transaction = []
        if self.validation(self.bank_name, self.account_number, self.card_number, self.balance):
            self.save_in_file()
            return 'Account created'
    
        

    @staticmethod
    def validation(bank_name, account_number, card_number, balance):
        b_n = ValidateBankName(bank_name)
        a_n = ValidateAccountNumber(account_number)
        c_n = ValidateCardNumber(card_number)
        c_b = ValidateBalance(balance)

        if a_n.check_account_number() or not a_n.check_int():
            raise AccountNumberException
        elif c_n.check_card_number() or not c_n.check_int():
            raise CardNumberException
        elif b_n.check_bank_name():
            raise BankNameException
        elif not c_b.check_int():
            raise BalanceException
        else:
            return True


    def save_in_file(self):
        if not os.path.exists('Account.csv'):
            with open('Account.csv', 'w', newline='') as cs:
                w = csv.writer(cs)
                w.writerow(['bank name', 'account number', 'balance', 'card number',
                             'f income', 'f cost' , 'transaction'])
                w.writerow([self.bank_name, self.account_number, self.balance, self.card_number,
                            [], [], self.transaction])
        else:
            with open('Account.csv', 'a', newline='') as cs:
                    w = csv.writer(cs)
                    w.writerow([self.bank_name, self.account_number, self.balance, self.card_number,
                            [], [], self.transaction])
    
    def get_information(self):
        with open('Account.csv', 'r') as cs:
            r = csv.DictReader(cs)
            self.counter =0
            for i in r:
                if i['account number'] == str(self.account_number):
                    self.bank_name = i['bank name']
                    self.balance = i['balance']
                    self.card_number = i['card number']
                    self.transaction = i['transaction']
                    break
                self.counter +=1
        
    def append_transaction(self, mode, new_transaction):
        # reading the csv file 
        df = pd.read_csv("Account.csv") 
        # updating the column value/data 
        if df.loc[self.counter, mode] == '[]':
            df.loc[self.counter, mode] = df.loc[self.counter][mode][:-1] + new_transaction + ']'
        else:
            df.loc[self.counter, mode] = df.loc[self.counter][mode][:-1] + ', ' + new_transaction + ']'
        # writing into the file 
        df.to_csv("Account.csv", index=False)

    def __str__(self) -> str:
        self.get_information()
        return f'Bank name is: {self.bank_name}\nBalance is: {self.balance}\nCard number is: {self.card_number}\nAccount number is: {self.account_number}'
