n = int(input())

for row in range(1,n+1):
    #spaces 
    for spaces in range(1,n-row+1):
        print(" ",end='')
    
    #ascending triangle 
    count = 1
    for asc in range(1,row+1):
        print(count,end='')
        count += 1

    #decsending 
    count2 = row-1
    for des in range(1,row-1 + 1):
        print(count2 , end='')
        count2 -= 1

    print()