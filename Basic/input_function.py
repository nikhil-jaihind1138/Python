# simple input function
# name = input("Enter the Name: ")
# print(f"Hello {name}")

# Taking integer Input
# age = int(input("Enter your Age: "))
# print(f"Your Age is {age}")

# Taking float input
# price = float(input("Enter the Price: "))
# print(f"Price of the trade is {price}")

# Multiple inputs in one line
# a, b = input("Enter two Values: ").split()
# print(a, b)

# Multiple inputs in one line with integer coonversion
a, b = map(int, input("Enter two Values: ").split())
sum = a+b
print(sum)