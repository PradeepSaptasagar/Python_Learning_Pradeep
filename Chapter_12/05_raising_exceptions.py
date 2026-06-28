a=int(input("enter a number:"))
b=int(input("enter a second number:"))
if(b==0):
    raise ZeroDivisionError("Cannot divide by zero")
else:
    print(f"The division is {a/b}")