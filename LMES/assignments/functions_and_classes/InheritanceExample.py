""" Parent Class """


class PersonParentClass:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


""" Printing parent class object attributes """

x = PersonParentClass("John", "Doe")
x.printname()

""" Child Class """


class Employee(PersonParentClass):
    # Constructor method
    def __init__(self, firstname, lastname, employee_id):
        # Calling parent constructor method
        super().__init__(firstname, lastname)
        self.employeeId = employee_id

    def print_employee_id(self):
        print(self.employeeId)


""" Printing child class object attributes """

emp = Employee("John", "Doe", 88)
emp.print_employee_id()
