# A stack is a linear data structure that follows LIFO Principle 
# Undo / Redo functionality in text editors 

#basic Operations - push , pop , peek/top , isEmpty

# Implementation of stack is using List 

stack = []

stack.append("Book 1")
stack.append("Book 2")
stack.append("Book 3")

print("Stack Top is ", stack[-1])

stack.pop()

print("Stack Top is ",stack[-1])
