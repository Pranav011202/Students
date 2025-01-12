import random 
change = input("Do You want to change the seed Value (YES/NO)")

if change == 'YES':
    seed_v = int(input("Enter the seed value: "))
else:
    seed_v = 6

random.seed(seed_v)
for i in range(5):
    print(random.randint(10,50))