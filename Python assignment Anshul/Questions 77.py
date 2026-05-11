'''Write a Python program to read a file line by line store it into a variable.'''

with open("write.txt", "r") as file:
    content = file.read()
    file.close()
print(content)
