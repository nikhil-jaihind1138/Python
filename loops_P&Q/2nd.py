""" calculate how many numbers are divisible by 7 from 1 to 100 """
i = 1
total = 0
while i <= 100:
    if i%7 == 0:
        print(i, end=" ")
        total += 1
    i += 1
print(f"\nTotal Numbers divisible by 7 between 1 to 100 is {total}")