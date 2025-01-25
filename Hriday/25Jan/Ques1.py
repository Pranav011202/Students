

word = input()

l1 = word.split()

l2 = []

for i in l1:
    l2.append(i[::-1])

result = " ".join(l2)
print(result)


