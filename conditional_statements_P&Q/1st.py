"""
Write a Python program that takes an integer input and prints whether it's positive, negative 
and consider 0 as positive
"""

num = int(input("Enter the Number: "))
if num >= 0:
    print(f"Number {num} is Positive")
else:
    print(f"Number {num} is Negative")