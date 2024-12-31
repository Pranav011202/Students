a = int(input())
b = int(input())
c = int(input())

#check if these three sides form a triangle or not 
if a+b > c and b + c > a and c + a > b :
    print("Yes ! it forms a triangle ")

    #if yes then I check if it is equilateral , isoceles or scalene 
    if a==b==c:
        print("It is equilateral")
    elif a==b or b==c or c==a:
        print("It is isoceles")
    else:
        print("Scalene")

else:
    print("It doesn't form a triangle ")