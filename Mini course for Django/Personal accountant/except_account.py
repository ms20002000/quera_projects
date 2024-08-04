import csv
import os.path

class AccountNumberException(BaseException):
    def __str__(self) -> str:
        return "Error: Account number already exists"


class CardNumberException(BaseException):
    def __str__(self) -> str:
        return "Error: Card number already exists"

class BankNameException(BaseException):
    def __str__(self) -> str:
        return "Error: bank name must have value"
    
class BalanceException(BaseException):
    def __str__(self) -> str:
        return "Error: Blance must be nember"
    
class AccountException(BaseException):
    def __str__(self) -> str:
        return "Error: Account number must be nember"
    
class CardException(BaseException):
    def __str__(self) -> str:
        return "Error: Card number must be nember"

class AmountofIncome(BaseException):
    def __str__(self) -> str:
        return f"Error: Amount of money must be nember"



class ValidateBankName:
    def __init__(self, bank_name) -> None:
        self.bank_name = bank_name
    
    def check_bank_name(self):
        if len(self.bank_name) <1:
            return True
        return False


class ValidateAccountNumber:
    def __init__(self, account_number) -> None:
        self.account_number = account_number

    def check_account_number(self):
        if not os.path.exists('Account.csv'):
            return False
        with open('Account.csv', 'r') as cs:
            r = csv.DictReader(cs)
            for i in r:
                if i['account number'] == str(self.account_number):
                    return True
            return False
        
    def check_int(self):
        try:
            return type(int(self.account_number)) == int
        except BaseException:
            raise AccountException
            

class ValidateCardNumber:
    def __init__(self, card_number) -> None:
        self.card_number = card_number

    def check_card_number(self):
        if not os.path.exists('Account.csv'):
            return False
        
        with open('Account.csv', 'r') as cs:
            r = csv.DictReader(cs)
            for i in r:
                if i['card number'] == self.card_number:
                    return True
            return False
        
    def check_int(self):
        try:
            return type(int(self.card_number)) == int
        except BaseException:
            raise CardException

class ValidateAmountOfIncome:
    def __init__(self, amount_of_money) -> None:
        self.amount_of_money = amount_of_money

    def check_amount_of_income(self):
        try:
            return type(float(self.amount_of_money)) == float
        except BaseException:
            raise AmountofIncome

class ValidateBalance:
    def __init__(self, amount_of_money) -> None:
        self.amount_of_money = amount_of_money

    def check_int(self):
        try:
            return type(float(self.amount_of_money)) == float
        except BaseException:
            raise BalanceException