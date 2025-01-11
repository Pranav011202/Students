def fib(n):
    n1 , n2 = 0 , 1 
    print(n1)
    print(n2)
    for i in range(3,n+1):
        nth = n1 + n2 
        print(nth)
        n1 = n2 
        n2 = nth 
        


n = int(input("Enter the terms you want to display "))

fib(n)