import math 

# Step 1 : Input the sides of the triangle 

a  = int(input("Enter the value of side a "))
b  = int(input("Enter the value of side b "))
c  = int(input("Enter the value of side c "))

# Step 2 : Calculate cosine values using the formula 

cosA = (b**2 + c**2 - a**2) / (2 * b * c)
# cosB = # do it on your own 
# cosC = # do it on your own 

A = math.degress(math.acos(cosA))
# B = 
# C = 

