# Open the file in read mode 
f = open("sample.txt","r")

content = f.read()

vowel_c = 0 
consonents_c = 0 
upper_c = 0 
lower_c = 0 

vowels = "aeiouAEIOU"

for i in content:
    if i.isalpha():
        if i in vowels:
            vowel_c += 1
        else:
            consonents_c += 1 
        
        if i.isupper():
            upper_c += 1
        else:
            lower_c += 1

f.close()          
            
print("The no of vowels is " , vowel_c)
print("The no of consonents is" , consonents_c)
print("The no of upper case is " ,upper_c)
print("The no of lower case is " ,lower_c)

