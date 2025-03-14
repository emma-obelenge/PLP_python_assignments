print("Welcome to the Simple Calculator Program")
print("This program only calculates for")
print("addition (+), subtraction (-), multiplication (x), and division (/)")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("what are you calculating for? (+, -, x, or /): ")
#parsing the user operator input
if(operator == "+"):
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
elif(operator == "-"):
    print(str(num1) + " - " + str(num2) + " = " + str(round((num1 - num2), 2)))
elif(operator == "x" or operator == "*"):
    print(str(num1) + " x " + str(num2) + " = " + str(round((num1 * num2), 2)))
elif(operator == "/"):
    print(str(num1) + " / " + str(num2) + " = " + str(round((num1 / num2), 2)))
else:
    print("invalid operator" + " " + str(num1) + " " + operator + " " + str(num2))
