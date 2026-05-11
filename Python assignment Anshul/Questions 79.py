'''Write a Python program to count the number of lines in a text file. '''

with open("write.txt", "r") as file:
    print("Number of lines in file:", len(file.readlines()))