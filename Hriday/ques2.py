#We have taken a nested list and treated it like a stack 
book_stack = [
    ["The Alchamist","Author-1"],
    ["The last train","Author-2"],
    ["Python book","Author-3"]
]

# Creating a menu driven program 
# We will ask user 1,2,3,4 
# 1 - new book add  ( we will append in the stack (nested list))
# 2 - removing the recently read book 
# 3 - viewing the last read book
# 4 - get out of the program 

while True:
    print("Welcome to Modern School's Library ")
    print("Select the following options ")
    print("1) To add a new book ")
    print("2) To remove the recently read book ")
    print("3) To view the last read book ")
    print("4) To log out of the portal ")

    choice = int(input("Enter your choice "))

    if( choice == 1 ):
        title = input("Enter the book Title ")
        author = input("Enter the author's Name ")
        book_stack.append([title,author])

    elif (choice == 2):
        book_stack.pop()

    elif (choice == 3):
        last_read = book_stack[-1]
        print(f"Your last read book is {last_read}")

    elif (choice == 4):
        print("Exiting the program and your final collection is ")
        print(book_stack)
        break

