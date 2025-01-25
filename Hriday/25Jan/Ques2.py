t1 = ("Hii" , "There" , "bro")
t2 = []
for i in t1:
    t2.append(i[::-1])
ans = "$".join(t2)

print(ans)