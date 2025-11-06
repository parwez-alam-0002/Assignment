# calculate factorial of given number
def fact(no):
    f=1
    while(no>=1):
        f=f*no
        no=no-1
    return f

print(fact(5))
