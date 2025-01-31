#for loop

# user_input = int(input("Enter a number:"))
# for i in range(1,11):
#     print(user_input * i)

#while loop

password = "yash"
input_password = input("enter your password:")

while password != input_password:
    input_password = input("enter your password:")
else:
    print("congrations")