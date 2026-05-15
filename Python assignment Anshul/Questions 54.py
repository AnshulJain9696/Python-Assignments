'''Write a Python program to check multiple keys exists in a dictionary'''

my_dict = {"name": "Anahul", "age": 22, "city": "Jaipur"}
keys = input("Enter keys separated by space: ").split()
for i in keys:
    if i in my_dict:
        print(f"Key '{i.upper()}' is present")
    else:
        print(f"Key '{i}' is not present")
