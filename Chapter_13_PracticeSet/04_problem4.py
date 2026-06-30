def divisibes(n):
    if(n%5==0):
        return True
    return False

a=[1,2,4654,35,55,4564,2182,8974]
f=list(filter(divisibes,a))
print(f)