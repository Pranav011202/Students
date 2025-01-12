# Finding the GCD using Euclidean Algorithm 

# Algorithm is -  gcd(n1,n2) = gcd(n1-n2,n2) given n1>n2 
def gcd(n1,n2):
    while(n1 != 0 and n2 != 0):
        if(n1>n2):
            n1 = n1-n2 
        else:
            n2 = n2-n1 
        if(n1 == 0):
            return n2 
        if(n2 == 0):
            return n1


n1 = int(input("Enter the first number "))
n2 = int(input("Enter the second number "))

print(gcd(n1,n2))