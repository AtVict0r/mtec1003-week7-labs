answer = str.casefold(input("Does it move? (y/n): "))
if answer == 'y': 
    answer = str.casefold(input("Should it move? (y/n): "))
    if answer == 'y':
        print("No problem.")
    elif answer == 'n':
        print("Then use duct tape!!!")
    else:
        print("Answer my question! You didn't type y or n.")
elif answer == 'n':
    answer = str.casefold(input("Should it move? (y/n): "))
    if answer == 'y':
        print("Then use lubricant!!!")
    elif answer == 'n':
        print("No problem.")
    else:
        print("Answer my question! You didn't type y or n.")
else:
    print("Answer my question! You didn't type y or n.")