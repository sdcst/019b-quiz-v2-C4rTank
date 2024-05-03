#!python3
"""
Write a program that sorts the values in this list and prints
the 3 highest numbers. You may use multiple print statements,
but you should try to incorporate a for loop and use 1 print
statement instead.
"""
numbers = [3,4,6,1,3,6,12,33,15,2,22,9,17]
numbers.sort()
print(numbers)

print("your largest numbers are", end=" ")
print(numbers[12], end=", ")
print(numbers[11], end=", ")
print(numbers[10], end="!") 

#done
