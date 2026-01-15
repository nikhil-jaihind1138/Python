""" Ask a number from user.
Print all Numbers from 1 to that number """

num = int(input("Enter the last Numebr: "))
if num == 1:
    print("It is the starting value give me the last value!!!")
elif num > 1:
    for i in range(1, num+1):
        print(i, end=" ")
else:
    for i in range(1, num-1, -1):
        print(i, end=" ")