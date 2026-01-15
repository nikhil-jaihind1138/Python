""" Ask two numbers x and y from user. 
If x < y then print all numbers from x to y, but if y < x then print all the numbers from y to x """

x = int(input("Enter the 1st Number: "))
y = int(input("Enter the 2nd Number: "))
if x < y:
    while x <= y:
        print(x)
        x = x+1

elif y < x:
    while y < x:
        print(y)
        y = y+1
        
else:
    print("Both numbers are equal.")