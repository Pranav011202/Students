#Initialize an empty stack 
stack = []

# We will make a user - driven program for a text editor stack 

while(True):
    print("WELCOME TO OUR TEXT EDITOR ")
    print("1) TYPE A NEW SENTENCE ")
    print("2) UNDO THE LAST SENTENCE ")
    print("3) PEEK AT THE NEXT UNDO ")
    print("4) CHECK IF THERE IS ANY ACTION LEFT FOR UNDO ")
    print("5) SHOW ALL THE SENTENCES ")
    print("6) LOG OUT ")

    choice = int(input("ENTER YOUR CHOICE "))

    if (choice == 1):
        sentence = input("Enter the sentence ")
        stack.append(sentence)
        
    elif (choice == 2):
        

