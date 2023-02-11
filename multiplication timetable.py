print("-------------------------------------------Welcome to YhawTech Timetable----------------------------------")
name = input("What is your name?")
print("Welcome", name)
continue_m = True
while continue_m:
    ourNum = int(input("Which number do you want the Multiplication timetable for?:"))
    ourRange = range(1, 13)
    for x in ourRange:
        result = ourNum * x
        print(ourNum, " * ", x, "=", result)
continue_m2 = True
while continue_m2:
    proceed = input("Would you like to continue?(y/n)").lower()
if proceed == "n":
    continue_m = False
    print('------------------------------------------------Thank you for your time-----------------------------------')
elif proceed == 'y':
    continue_m = True
else:
    print('Invalid input try again')
    continue_m2 = True
           
