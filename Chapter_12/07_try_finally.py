try:
    a=int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyy")
    print(v)

finally:
    print("Finally loop")
