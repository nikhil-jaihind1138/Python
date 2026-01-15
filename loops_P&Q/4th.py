""" Write a program to calculate the sum of all numbers divisible by 4 from 20 to 50 """

i = 20
sum = 0
while i <= 50:
    if i % 4 == 0:
        print(i, end=" ")
        sum += i
    i += 1
print(f"\nSum of all numbers: {sum}")