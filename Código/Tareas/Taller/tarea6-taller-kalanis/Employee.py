class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def  displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def getName(self):
        return self.name

    def setSalary(self,newSalary):
        self.salary = newSalary

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp = Employee("Andres",1000000)
print(emp.getName())
emp.setSalary(0)
emp.displayEmployee()
