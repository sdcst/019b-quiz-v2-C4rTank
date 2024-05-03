"""
Write a program that uses a for loop.
Each iteration will ask the user to enter a name
Add the input to the provided list
"""
names = []

for nam in range(10):
    nam = input("Please input name: ")
    names = names + [nam]
    print(names)

#done