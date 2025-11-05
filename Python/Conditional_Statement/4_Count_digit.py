# check if the given number is single digit, double -digit or more

number = int(input("Enter a number"))
count=0
while(number>0):
    count+=1
    number//=10

print(f"It is a {count} digit number")
