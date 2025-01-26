n = int(input("Enter the value of rows "))

flip = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(flip,end="")
        flip = 1 - flip 
        
    print()

