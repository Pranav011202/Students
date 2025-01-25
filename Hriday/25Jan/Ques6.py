runs = (0, 6, 1, 3, 2, 6, 0, 0, 1, 6, 0, 1, 4, 3, 1, 0, 0, 0, 6, 1, 3, 2, 6, 0)

dict1 = {}

for i in runs:
    if i in dict1:
        dict1[i] +=1
    else:
        dict1[i] = 1 

print(dict1)

