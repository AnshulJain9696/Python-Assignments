'''Write a Python program to append text to a file and display the text. '''

with open("write.txt", "a") as file:
    file.write("\nThis text is appended.")

with open("write.txt", "r") as file:
    print(file.read())