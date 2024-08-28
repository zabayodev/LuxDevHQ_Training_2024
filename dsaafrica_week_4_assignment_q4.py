'''
A bigram is a sequence of two adjacent elements from a string of tokens, which can be words, 
letters, or characters. Below is an approach to create a function in Python that takes a string and returns a list
of bigrams.
'''
def generate_bigrams(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Use list comprehension to create bigrams
    bigrams = [(words[i], words[i+1]) for i in range(len(words) - 1)]
    
    return bigrams


input_string = "We are doing data engineering bootcamp at Lux Academy"
bigrams = generate_bigrams(input_string)
print(bigrams)

# The bigrams are generated using the split methods