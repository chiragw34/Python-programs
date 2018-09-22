
class Employee:

    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
        self.email=name + '.' + age + '@company.com'

    def display(self):
        print(self)

emp1=Employee(input("enter the name:"),input("enter the salary:"),input("enter the age:"))
emp2=Employee(input("enter the name:"),input("enter the salary:"),input("enter the age:"))
print(emp1.__dict__)
print(emp2.__dict__)
