""" Write a program to find the factorial of a number
and ask the number from the user """

num = int(input("Enter the number : "))
i = num
fact = 1
while num >= 1:
    print(num, end=" X ")
    fact = fact*num
    num = num-1
print(f"\nFactorial value of the number {i} is {fact}")