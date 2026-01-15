""" Write a program that takes 2 numbers as input 
and checks if the first number is divisible by second number or not """

x = int(input("Enter the 1st Number: "))
y = int(input("Enter the 2nd Number: "))

if x%y == 0:
    print(f"{x} is dvisible by {y}")
else:
    print(f"{x} is not divisible by {y}")