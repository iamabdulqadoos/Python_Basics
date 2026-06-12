name = ["Abdul", "Qadoos", "Ali", "Khan", "Abdul", "Qadoos", "Ali", "Khan"]

print(name)
print(name[0])  # Accessing the first element
print(name[3])  # Accessing the fourth element
print(name[-1])  # Accessing the last element
print(name[-8]) # Accessing the first element using negative indexing
print(len(name))  # Length of the list
print(name.append("Aq"))  # Adding an element to the end of the list
print(name)
print(name.insert(2, "Aq"))  # Inserting an element at a specific index
print(name)
print(name.remove("Aq"))  # Removing the first occurrence of an element
print(name)
print(name.count("Abdul"))  # Counting Duplicates of an element
print(name.count("Aq"))  # Counting Duplicates of an element
print(name.index("Ali"))  # Finding the index of the first occurrence of an element

print(name[:4])  # Slicing the list from index 0 to 3
print(name[2:])  # Slicing the list from index 2 to the end
print(name[:4])  # Slicing the list from the beginning to index 3
print(type(name))  # Checking the type of the List 