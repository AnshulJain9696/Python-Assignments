'''How Do You Check the Presence of a Key in A Dictionary?'''

my_dict = {"name": "Anshul; jain", "age": 22, "city": "Bhilwara"}
if  my_dict.get("age") :
    print("Key is present")
else:
    print("Key is not present")
