# 4.⁠ ⁠Write a program which should copy only those lines from a file which begin
# with an uppercase letter. (consider total five lines to execute the program
# and start 3 lines with uppercase in first( .txt) file.)


source = open("cont.txt","r+")
dest = open("destination.txt","w")
l = source.readlines()

for i in l:
    if (i[0].isupper()):
        dest.write(i)

dest.close()
source.close()
    
