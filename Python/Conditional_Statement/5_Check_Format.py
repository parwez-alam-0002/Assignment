# check if the input is in uppercase, lowercase or indigit
data=input("Enter you text : ")
if(data.isdigit()):
    print("It is a digit")
elif (data.isupper()):
    print("In uppercase format.")
elif data.islower():
    print("In lowercase format")
