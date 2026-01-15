""" Ask a Number from the user and print the multiplication table of that number """

num = int(input("Enter the Number whose multiplication table you want: "))
i = 1
while i<=10:
    print(f"{num} x {i} = {num*i}")
    i+=1