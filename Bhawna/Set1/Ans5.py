#first we will take the input of m and n 
m = int(input("Enter the dividend"))
n = int(input("Enter the divisor "))

q , r = divmod(m,n)

if(r == 0):
    print("It is divisible ")
else:
    print("It is not ")