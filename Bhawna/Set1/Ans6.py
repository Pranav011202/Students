#ALGORITHM 

#Step 1 ) List declare 
#Step 2) LOOP 10 times and every time you will take input from user and append it in list 
#Step 3 ) Sort the list 
#Step 4) List[9] - List[0]
#Step  5 ) List[9] / List[0]

List = []  

for i in range(10):
    num = int(input(f"Enter the number {i+1} "))
    List.append(num)

p = max(List)
q = min(List)

#HOW MUCH LARGE IS MAX FROM MIN

print(f"The difference between max and min is {p-q}")

#CALCULATING HOW MANY TIMES MAX IS OF MIN 

print(f"max is {p/q} times than that of min")


