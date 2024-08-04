import datetime
from account import Account
import pandas as pd
from except_account import ValidateAmountOfIncome, AmountofIncome

class Income(Account):
    def __init__(self, account_number) -> None:
        super().__init__(account_number)
        self.get_information()

    def add(self, category, new_income, amount_of_income, frequent_activity:str = 'no'):
        self.category = category
        self.new_income = new_income
        self.amount_of_income = amount_of_income
        self.frequent_activity = frequent_activity.lower()
        self.validation()
        self.choose_category()

    def old_incomes(self):
        df = pd.read_csv("Account.csv") 
        self.old_incomes_list = df.loc[self.counter, 'f income'][1:-1].split(',')
        indexes = [i for i in range(len(self.old_incomes_list))]
        return list(zip(indexes, self.old_incomes_list))
    
    def add_old_income(self, index, amount_of_income):
        self.amount_of_income = amount_of_income
        self.validation()
        new_transaction = f'Income; {self.old_incomes_list[index]} at {datetime.datetime.now()} added'
        self.append_transaction(mode= 'transaction', new_transaction= new_transaction)
        self.add_balance()


    def validation(self):
        check_amount_of_income = ValidateAmountOfIncome(self.amount_of_income)
        if not check_amount_of_income.check_amount_of_income():
            raise AmountofIncome
        

    def choose_category(self):
        match self.category:
            case 1: self.category = 'Salary'
            case 2: self.category = 'Interest'
            case 3: self.category = 'Inheritance'
            case 4: self.category = 'Etc'
        self.save_transaction()
        
    
    def save_transaction(self):
        new_transaction = f'Income; {self.category}: {self.new_income} at {datetime.datetime.now()} added'
        self.append_transaction(mode= 'transaction', new_transaction= new_transaction)
        self.add_balance()
        if self.frequent_activity == 'yes':
            self.append_transaction(mode= 'f income',new_transaction= self.new_income)


    def add_balance(self):
        df = pd.read_csv("Account.csv") 
        df.loc[self.counter, 'balance'] = int(self.balance) + int(self.amount_of_income)
        df.to_csv("Account.csv", index=False)
    


class Cost(Account):
    def __init__(self, account_number) -> None:
        super().__init__(account_number)
        self.get_information()
        

    def add(self, category, new_cost, amount_of_cost, frequent_activity:str = 'no'):
        self.category = category
        self.frequent_activity = frequent_activity
        self.new_cost = new_cost
        self.amount_of_cost = amount_of_cost
        self.validation()
        self.choose_category()

    
    def choose_category(self):
        match self.category:
            case 1: self.category = 'Clothing'
            case 2: self.category = 'Food'
            case 3: self.category = 'Car'
            case 4: self.category = 'Etc'
        self.save_transaction()

    def save_transaction(self):
        new_transaction = f'Cost; {self.category}: {self.new_cost} at {datetime.datetime.now()} added'
        self.append_transaction(mode= 'transaction', new_transaction= new_transaction)
        self.minus_balance()
        if self.frequent_activity == 'yes':
            self.append_transaction(mode= 'f cost',new_transaction= self.new_cost)

    def old_cost(self):
        df = pd.read_csv("Account.csv") 
        self.old_cost_list = df.loc[self.counter, 'f cost'][1:-1].split(',')
        indexes = [i for i in range(len(self.old_cost_list))]
        return list(zip(indexes, self.old_cost_list))
    
    def add_old_cost(self, index, amount_of_cost):
        self.amount_of_cost = amount_of_cost
        self.validation()
        new_transaction = f'Cost; {self.old_cost_list[index]} at {datetime.datetime.now()} added'
        self.append_transaction(mode= 'transaction', new_transaction= new_transaction)
        self.minus_balance()

    def validation(self):
        check_amount_of_cost = ValidateAmountOfIncome(self.amount_of_cost)
        if not check_amount_of_cost.check_amount_of_income():
            raise AmountofIncome
    
    def minus_balance(self):
        df = pd.read_csv("Account.csv") 
        df.loc[self.counter, 'balance'] = int(self.balance) - int(self.amount_of_cost)
        df.to_csv("Account.csv", index=False)