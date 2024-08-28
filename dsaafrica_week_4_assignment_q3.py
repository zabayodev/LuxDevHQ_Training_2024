'''
A compound data type in Python is a data structure that can hold multiple values, often of different types, 
within a single object. These data types allow you to group together a related data and work with them as
a unit. The main compound data types in Python are lists, tuples, dictionaries and sets.
'''
# 1. List
# A list is an ordered collection of elements that can hold items of different types. 
# Lists are mutable which means that you can change their content (e.g. add, remove, or modify elements) of the list.

my_list = [1, 'apple', 3.14, True]
print(my_list)

# 2. Tuple
# A tuple is similar to a list in that it is an ordered collection of elements, 
# but tuples are immutable, meaning once they are created, their content cannot be changed.

my_tuple = (2, 'banana', 7.5, False)
print(my_tuple)

# 3. Dictionary
# A dictionary is an unordered collection of key-value pairs. Each key in a dictionary must be unique, 
# and it is used to retrieve its corresponding value.

my_dict = {'name': 'Alice', 'age': 30, 'is_student': False}
print(my_dict)