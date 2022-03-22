choice = str.casefold(input("Do you want cake? (y/n) "))
if choice == 'y':
    print("Have some cake.")
elif choice == 'n':
    print("No cake for you.")
else:
    print("Sorry, I don't understand your response.")