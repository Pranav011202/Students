fullname = input("Enter the full name ")

l1 = fullname.split()

#["Mohandas" , "karamchand" , "Gandhi"]

l2 = []
for i in l1:
    l2.append(i[0].upper())

initial = ".".join(l2)

print(initial)
