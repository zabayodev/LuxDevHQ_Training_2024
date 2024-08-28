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

d = {
    'a': ['x', 'y', 'z'],
    'b': ['y', 'z', 'a'],
    'c': ['a', 'b', 'c'],
}

result = closest_key(d, 'z')
print(result)
