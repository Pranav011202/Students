#First we will take sides of the triangle 

a = int(input("Enter the first side length"))
b = int(input("Enter the second side length"))
c = int(input("Enter the theory side length"))

sides = [a,b,c]
sides.sort() #ascending order sorting 

#checking using pythagprous theoram 

if(sides[2]**2 == sides[0]**2 + sides[1]**2):
    print("It is a right angle triangle ")
else:
    print("It is not a right angle triangle ")



