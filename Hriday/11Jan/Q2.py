def isPrime(n):
    for i in range(2,n):
        if(n % i == 0):
            return False 
    return True

n = int(input("Enter the number "))

if(isPrime(n)):
    print("It is a Prime Number ")
else:
    print("It is not a Prime Number ")