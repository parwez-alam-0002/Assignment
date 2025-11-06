# check if the input is in uppercase, lowercase or indigit
def checkData(text : str)-> str:
    if text.isdigit():
        return "Digit"
    elif text.islower():
        return "LowerCase"
    elif text.isupper():
        return "UpperCase"
    else:
        return "None"


info=input("Enter the data : ")
print(checkData(info))
