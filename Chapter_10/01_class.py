class Employee:
    language="Py" # this is a class attribute
    salary=99999999

pradeep=Employee()
pradeep.name="Pradeep" # This is an instance attribute
print(pradeep.name,pradeep.language,pradeep.salary)

harry=Employee()
harry.name="Harry"
print(harry.language,harry.name,harry.salary)

# Here name is an object attribute and salary and language are class attributes as they directly belong to the class
