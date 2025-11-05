# take marks from user and create grade system
# >=90 A grade, >=75 B grade, >=50 C grade else Fail

mark=int(input("Enter you mark : "))
if mark >= 90:
    print("A grage")
elif mark >= 75:
    print("B Grade")
elif mark >= 50 :
    print("C Grade")
else:
    print("Fail")
