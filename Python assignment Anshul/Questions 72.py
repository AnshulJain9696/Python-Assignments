'''Write a Python program to read an entire text file. '''

with open("write.txt", "w") as file:
    print(file.write("Hello, I am Anshul."))

with open("write.txt", "r") as file:
    print(file.read())