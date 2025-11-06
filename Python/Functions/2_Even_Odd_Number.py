# check if the given number is even or odd
def even_odd(number: int)->str:
    if number % 2:
        return "Odd"
    else:
        return "Even"

no=int(input("Enter a number"))
print(even_odd(no))
