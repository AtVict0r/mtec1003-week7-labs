num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operator = str.casefold(input("Enter an operator (add / sub / mul / div / mod): "))
if operator == "add":
    print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2))
elif operator == "sub":
    print("The difference of " + str(num1) + " and " + str(num2) + " is " + str(num1 - num2))
elif operator == "mul":
    print("The product of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2))
elif operator == "div":
    print("The quotient of " + str(num1) + " and " + str(num2) + " is " + str(num1 / num2))
elif operator == "mod":
    print("The remainder of " + str(num1) + " and " + str(num2) + " is " + str(num1 % num2))
else:
    print("Invalid operator")