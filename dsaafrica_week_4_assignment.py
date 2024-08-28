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
    
    def size(self):
        return len(self.items)
    
    def palindrome_check(input_string):
        stack = Stack()
        cleaned_string = input_string.replace(" ", "").lower()
        for char in cleaned_string:
            stack.push(char)
        
        reversed_string = ''
        while not stack.is_empty():
            reversed_string += stack.pop()
        
        return cleaned_string == reversed_string