units=int(input("enter the number of electrical units consumed: "))
if units<50:
    amount=units*2.60
    surcharge=25
elif units<=100:
    amount=130+(units-50)*3.25
    surcharge=35
elif units<=200:
    amount=130+162.5+(units-100)*5.26
    surcharge=45
else:
    amount=130+162.5+526+(units-200)*7.87
    surcharge=55
total_amount=amount+surcharge
print("the total amount to be paid is: ", total_amount)
