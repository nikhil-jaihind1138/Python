""" Calculate how many numbers are divisible by both 6 and 7 from 1 to 200"""

i = 1
total = 0
while i <= 200:
    if i%6 == 0 and i%7 == 0:
        print(i, end=" ")
        total += 1
    i = i+1
print(f"\nTotal Numbers divisible by both 6 and 7 from 1 to 200 are {total}")