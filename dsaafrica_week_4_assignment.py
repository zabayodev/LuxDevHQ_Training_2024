'''
A palindrome is a sequence of characters that reads the same forward and backword
the reverse of the word looks like the original word.

'''
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def is_palindrome(input_string):
    stack = Stack()
    # Remove spaces and convert to lowercase for a case-insensitive check
    cleaned_string = input_string.replace(" ", "").lower()

    # Push all characters of the string into the stack
    for char in cleaned_string:
        stack.push(char)

    # Rebuild the string by popping characters from the stack
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    # Compare the cleaned string with the reversed string
    return cleaned_string == reversed_string

# Example usage
def main():
    input_string = "A man a plan a canal Panama"
    result = is_palindrome(input_string)
    if result:
        print(f"'{input_string}' is a palindrome.")
    else:
        print(f"'{input_string}' is not a palindrome.")

if __name__ == "__main__":
    main()