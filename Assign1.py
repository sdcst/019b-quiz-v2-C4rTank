#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program

num = 0
total = 0

for n in range(5):
    num = float(input("Please input a 5 values: "))
    total = num  + total
    print(total)

#done