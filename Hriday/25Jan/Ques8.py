n = int(input())

for i in range(1,n+1):
    #spaces 
    for k in range(n-i):
        print(" ",end="")
    #stars 
    for j in range(1,2*i-1 + 1):
        print("*",end="")
     
    print()

    