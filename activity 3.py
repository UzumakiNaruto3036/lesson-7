print('which ride do you want?')
print('1 bike')
print('2 car')
choice=int(input('enter your choice: '))
if choice==1:
    print('what kind of bike do you want?')
    print('1 SCOOTER')
    print('2 scooty')
    choice2=int(input('enter your choice: '))
    if choice2==1:
        print('you have selected SCOOTER')
    else:
        print('you have selected scooty')
elif choice==2:
    print('what kind of car do you want?')
    print('1 XUV')
    print('2 sedan')
    choice3=int(input('enter your choice: '))
    if choice3==1:
        print('you have selected XUV') 
    else:
        print('you have selected sedan')
else:
    print('invalid input')  
   