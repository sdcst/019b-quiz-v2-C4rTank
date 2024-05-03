#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""



for n in range(10):
    num = float(input("Please input a 10 values: "))
    if num > 0:
        print('that is a positive number')
    elif num < 0:
        print('that is a negative number')

#done