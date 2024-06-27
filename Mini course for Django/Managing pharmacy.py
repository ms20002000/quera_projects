class Drug:
    def __init__(self, name: str, amount: int, price: int):
        self.name = name
        self.amount = amount
        self.price = price


class Pharmacy:
    def __init__(self, name: str):
        self.name = name
        self.employees = []
        self.drugs = []

    def add_drug(self, drug: Drug):
        self.drugs.append(drug)

    def add_employee(self, first_name: str, last_name: str, age: int):
        self.employees.append({"first_name": first_name, "last_name": last_name, "age": age})

    def total_value(self) -> int:
        m =0
        for i in self.drugs:
            m+= i.amount* i.price
        return m

    def employees_summary(self) -> str:
        j =1
        s = f'Employees:\n'
        for i in self.employees:
            s += (f'The employee number {j} is {i['first_name']} {i['last_name']} who is {i['age']} years old.\n')
            j+=1
        return s