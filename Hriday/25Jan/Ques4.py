# students = [[hriday,25] ,[Pranav,30] , [Hrishit,40]]

students = []
while True:
    print("Menu: ")
    print("1) Append a student ")    
    print("2) Display all students ")
    print("3) Calculate and dispaly average marks ")
    print("4) Exit ")

    choice = int(input("Enter the choice "))

    if(choice == 1):
        name = input("Enter the name ")
        marks = float(input("Enter the marks "))
        students.append([name , marks])
    elif choice == 2:
        for innerList in students:
            print(f"Name : {innerList[0]} , Marks : {innerList[1]}")
    elif choice == 3:
        t_marks = 0 
        for i in students:
            t_marks += i[1]

        average = t_marks / len(students) 

        print("Average Students " , average)
    
                


