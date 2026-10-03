medical_cause=input("do you have a medical cause? (y/n) ")
if medical_cause.lower() == "y":
    print("student is allowed to attend exams")
elif medical_cause.lower() == "n":
    attendance=int(input("enter your attendance percentage: ")) 
    if attendance >= 75:
        print("student is allowed to attend exams")
    else:
        print("student is not allowed to attend exams")
else:
    print("invalid input")
