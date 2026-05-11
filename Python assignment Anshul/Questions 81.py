'''Write a Python program to write a list to a file. '''

my_list = ["apple", "banana", "cherry", "date"]
with open("write.txt", "a") as file:
    print(file.writelines(my_list))