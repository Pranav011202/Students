#file object is returned when we use a open function . 
#This file object acts a bridge between python program and file of our system 
#Using this object we can perform various operations like reading , writing , appending , closing 

file_o = open("sample3.txt","r") # it will open the file and read mode and returns an object in the variable file_o

print(file_o.name)
print(file_o.mode)
print(file_o.closed) # check if the file is closed or not 

file_o.close() # closes the file

print(file_o.closed)




