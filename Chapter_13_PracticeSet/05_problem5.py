from functools import reduce
l=[1,2,46,35,55,64,82,89]
def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))
