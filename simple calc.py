num1, operator, num2 = input("Enter Calculation: ").split()

# Convert the trings into integers
num1= float(num1)
num2 = float(num2)
# if they enter +, -, *, /, then we need to provide output based on operator

if operator == "+":
    print("{} + {} = {}".format(num1,num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1,num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1,num2, num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1,num2, num1/num2))
else:
    print("Syntax error")

