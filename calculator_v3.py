## calculator v3.0
# num1 = input("First Number: ")
# num2 = input("Second Number: ")
# action = input("Add action: ")
# intNum1 = int(num1)
# intNum2 = int(num2)
# if action == "+":
#     print(intNum1+intNum2)
# elif action == "-":
#     print(intNum1-intNum2)
# elif action == "*":
#     print(intNum1*intNum2)
# elif action == "/":
#     print(intNum1/intNum2)

# refactored calculator v3.0
num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
action = input("Add action: ")
if action == "+":
    result = num1+num2
elif action == "-":
    result = num1-num2
elif action == "*":
    result = num1*num2
elif action == "/":
    result = num1/num2
print(result)
