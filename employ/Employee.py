class Employee:
    def __init__(self,code,name,salary,age):
        self.code= code
        self.name=name
        self.salary= salary
        self.age=age
    def income(self):
        result= 0.9*12*self.salary
        return result
    def increaseSalary(self):
        if amount > 0:
            self.salary=self.salary + amount
    def display(self):
        print(f"code: {self.code},name: {self.name}, salary: {self.salary}, age: {self.age}, income: {self.income()}\n")
