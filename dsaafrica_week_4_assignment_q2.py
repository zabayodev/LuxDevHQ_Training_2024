'''
List comprehension is a concise way to create lists in Python. It provides a more readable and compact syntax for
generating lists compared to traditional methods like loops. 

'''
# Creating a list comprehension expression
'''
[expression for item in iterable if condition]
'''
#expression: The value to include in the new list.
#item: The variable representing each element in the iterable.
#iterable: The collection to loop over such as a list and a range.
#condition which is optional is a filter that determines if an item should be included in the new list.

# Example #1.  creating a list of squares for numbers from 0 to 9
squares = []
for i in range(10):
    squares.append(i**2)
#print(squares)

# Example #2.  creating a list of even numbers from 0 to 9.
evens = []
for i in range(10):
    if i % 2 == 0:
        evens.append(i)
#print(evens)


