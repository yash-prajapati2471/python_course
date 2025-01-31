# age = 12

# if age >= 18:
#     print("you are an adult")

# elif age >= 12:
#     print("you are center")

# else:
#     print("you are not adult")

first = int(input("Enter first number"))
second = int(input("Enter second number"))
operator = input("enter operator (+,-,*,/):")

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)

elif operator == "*":
    print(first * second)

elif operator == "/":
    print(first / second)

else:
    print("not a value match")
