class Employee:
    language="Py" # this is a class attribute
    salary=99999999
 
    def __init__(self,name,salary,language): # dunder method which is automatically called
        self.name=name
        self.salary=salary
        self.language=language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print("Good Morning")

pradeep=Employee("Pradeep",99999999000,"JavaScript")
pradeep.name="Pradeep" # This is an instance attribute
print(pradeep.name,pradeep.salary,pradeep.language)

# rohan=Employee()
