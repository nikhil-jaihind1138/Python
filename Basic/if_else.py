"""
Ask the user for the marks of his/her in both subjects physics and chemistry
and display PASS if the student is passed in both subjects
"""

m1 = int(input("Enter the marks of the Physics: "))
m2 = int(input("Enter the marks of the Chemistry: "))
if m1>=33 and m2>=33:
    print("You are PASS")
else:
    print("You are FAIL")