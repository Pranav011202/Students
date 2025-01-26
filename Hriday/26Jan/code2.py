word = input("Enter a string ")

for i in range(1,len(word) + 1):
    #spaces 
    print(" "*(len(word)-i),end="")
    #letters
    print(word[:i])

