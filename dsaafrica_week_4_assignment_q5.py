'''To solve this problem, the function closest_key takes a dictionary and a target letter as input.
The function will iterate through the dictionary, check which key has the target letter closest to the beginning of
its list and return that key.
'''
def closest_key(d, target):
    closest = None
    # Start with infinity so any index will be smaller
    min_index = float('inf')  

    for key, value_list in d.items():
        if target in value_list:
            # Get the index of the target in the list
            index = value_list.index(target)  
            if index < min_index:
                min_index = index
                closest = key

    return closest
# Testing the feasibility of the function
d = {
    'a': ['x', 'y', 'z'],
    'b': ['y', 'z', 'a'],
    'c': ['a', 'b', 'c'],
}

result = closest_key(d, 'z')
print(result)
'''
The function initializes closest to None and min_index to infinity.
It iterates over each key-value pair in the dictionary.
For each list in the dictionary, it checks if the target letter exists.
If the target letter is found, the function calculates its index in the list.
If this index is smaller than the currently stored min_index, the function updates min_index and sets closest to the current key.
The function returns the key that has the target letter closest to the beginning of the list.
In the provided example, the letter 'a' appears in the list for key 'c' at index 0, which is closer to the beginning compared to its position in other lists. Therefore, the function returns 'c'.

'''
