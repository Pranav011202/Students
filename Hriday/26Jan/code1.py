def fact(n):
    ans = n
    for i in range(n-1,0,-1):
        ans = ans * i 
    
    return ans

x = float(input("Enter the value of x in radians "))
n = int(input("Enter the number of terms "))

sign = -1
ans = 0
for i in range(n):
    term = (x ** (2*i + 1)) / fact(2*i + 1)
    ans += sign * term
    sign *= -1


