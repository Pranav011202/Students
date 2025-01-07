def is_balanced(expression):
    stack = []

    for i in expression:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0 


expression = input("Enter the expression with parenthesis ")

if is_balanced(expression):
    print("The expression has balanced paranthesis ")
else:
    print("The expression does not have balanced paranthesis ")

