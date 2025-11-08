'''Employee Salary Calculator
    create class Employee with name,salary and bonus
    create constructor
    add method total_salary to retun total salary including bonus.'''

class SalaryCalculator:
    def __init__(self,name,salary,bonus):
        self.name=name
        self.salary=salary
        self.bonus=bonus 
    
    def totalSalary(self)->float:
        print(f'{self.name} your salary is : ',end=" ")
        return self.salary+self.bonus 
    

emp=SalaryCalculator("Jhon Doe", 10000.00,1000)
print(f'{emp.totalSalary()}')
