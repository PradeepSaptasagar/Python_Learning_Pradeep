class Employee:
    language="Py" # this is a class attribute
    salary=99999999

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Morning")

pradeep=Employee()
pradeep.language="JavaScript" # This is an instance attribute
pradeep.greet()
pradeep.getInfo()

# Employee.getInfo(pradeep)
