## calculator v4.0
# expresion = input("Expresion: ").strip() # 5+2 or 10*7
# num1,action,num2 = list(expresion)
# num1 = int(num1)
# num2 = int(num2)
# if action == "+":
#     result = num1+num2
# elif action == "-":
#     result = num1-num2
# elif action == "*":
#     result = num1*num2
# elif action == "/":
#     result = num1/num2
# print(f"{expresion}={result}")

# refactored calculator v4.0
expresion = input("Expresion: ").strip()
result = eval(expresion)
print(f"{expresion}={result}")

