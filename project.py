import random

import mysql.connector as msc

def Teacher():
    print("----Teacher Menu	")
    print("1.Add Teacher") 
    print("2.Delete Teacher") 
    print("3.Add class") 
    print("4.Delete class") 
    print("5.Generate timetable")
    print("Enter any number to go back") 
    print("	")
    b=int(input("Enter what you want to do:- ")) 
    def AddTeacher():
        try:
            id=int(input("Enter teacher id:- ")) 
            n=input("Enter teacher name:- ") 
            s=input("Enter subject:- ") 
            p=input("Enter post:- ") 
            sal=int(input("Enter salary:- ")) 
            cl1=int(input("Enter class teaching 1:- ")) 
            cl2=int(input("Enter class teaching 2:- "))
            d=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c=d.cursor()
            c.execute("insert into teacher_details values ({},'{}','{}','{}',{},{},{})".format(id,n,s,p,sal,cl1,cl2)) 
            d.commit()
        except ValueError:
            print("Enter appropriate values") 
        except:
            print("An unexpected error occured") 
    def DelTeacher():
        try:
            idd=int(input("Enter teacher id:-")) 
            d=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c=d.cursor()
            c.execute("delete from teacher_details where Teacher_ID={}".format(idd)) 
            d.commit()
        except ValueError:
            print("Enter appropriate values") 
        except:
            print("An unexpected error occured") 
    def AddClass():
        try:
            cl=int(input("Enter class:- ")) 
            sec=input("Enter section:- ") 
            clt=input("Enter classtype:- ") 
            sub1=input("Enter main subject 1:- ")
            sub2=input("Enter main subject 2:- ") 
            sub3=input("Enter main subject 3:- ") 
            sub4=input("Enter main subject 4:- ") 
            sub5=input("Enter main subject 5:- ") 
            sub6=input("Enter additional subject 1:- ") 
            sub7=input("Enter additional subject 2:- ") 
            sub8=input("Enter additional subject 3:- ") 
            per=int(input("Enter no. of periods:- "))
            d=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c=d.cursor()
            c.execute("insert into student_details values ({},'{}','{}',{},'{}','{}','{}','{}','{}','{}','{}','{}')".format(cl,sec,clt,per,sub1,sub2,sub3,sub4,sub5,sub6,sub7,sub8))
            d.commit() 
        except ValueError:
            print("Enter appropriate values") 
        except:
            print("An unexpected error occured")
    def DelClass():
        try:
            cld=int(input("Enter class:- ")) 
            secd=input("Enter section:- ")
            d=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c=d.cursor()
            c.execute("delete from student_details where Class={} and Section='{}'".format(cld,secd)) 
            d.commit()
        except ValueError:
            print("Enter appropriate values") 
        except:
            print("An unexpected error occured")

    def GenTT():
        d=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
        c=d.cursor()
        cle=int(input("Enter class:- ")) 
        sece=input("Enter sec:- ")
        c.execute("Select Main_Sub1 from Student_details where Class={} And Section='{}'".format(cle,sece)) 
        if cle==12 and sece in ("aA"):
            a=c.fetchall() 
            Pe1=a[0][0]
            c.execute("Update 12A set P1='{}'".format(Pe1))

            l=["Phy","Math","Chem","Eng"] 
            x1=random.randint(0,3)
            c.execute("Update 12A set P2='{}' where day='monday'".format(l[x1])) 
            x2=random.randint(0,3)
            c.execute("Update 12A set P3='{}' where day='monday'".format(l[x2])) 
            x3=random.randint(0,3)
            c.execute("Update 12A set P4='{}' where day='monday'".format(l[x3])) 
            x4=random.randint(0,3)
            c.execute("Update 12A set P5='{}' where day='monday'".format(l[x4]))
            
            x5=random.randint(0,3)
            c.execute("Update 12A set P6='{}' where day='monday'".format(l[x5])) 
            x6=random.randint(0,3)
            c.execute("Update 12A set P7='{}' where day='monday'".format(l[x6])) 
            x7=random.randint(0,3)
            c.execute("Update 12A set P8='{}' where day='monday'".format(l[x7]))
            l1=["Phy","Math","Chem","Eng","Phy/Chem PR"] 
            x8=random.randint(0,4)
            c.execute("Update 12A set P2='{}' where day='tuesday'".format(l1[x8])) 
            x9=random.randint(0,4)
            c.execute("Update 12A set P3='{}' where day='tuesday'".format(l1[x9])) 
            x10=random.randint(0,4)
            c.execute("Update 12A set P4='{}' where day='tuesday'".format(l1[x10])) 
            x11=random.randint(0,4)
            c.execute("Update 12A set P5='{}' where day='tuesday'".format(l1[x11])) 
            x12=random.randint(0,4)
            c.execute("Update 12A set P6='{}' where day='tuesday'".format(l1[x12])) 
            x13=random.randint(0,4)
            c.execute("Update 12A set P7='{}' where day='tuesday'".format(l1[x13])) 
            x14=random.randint(0,4)
            c.execute("Update 12A set P8='{}' where day='tuesday'".format(l1[x14]))
            l2=["Phy","Math","Chem","Eng","Bio/CS","PHE/PAI","Lib"] 
            x15=random.randint(0,6)
            c.execute("Update 12A set P2='{}' where day='wednesday'".format(l2[x15])) 
            x16=random.randint(0,6)
            c.execute("Update 12A set P3='{}' where day='wednesday'".format(l2[x16])) 
            x17=random.randint(0,6)
            c.execute("Update 12A set P4='{}' where day='wednesday'".format(l2[x17])) 
            x18=random.randint(0,6)
            c.execute("Update 12A set P5='{}' where day='wednesday'".format(l2[x18])) 
            x19=random.randint(0,6)
            c.execute("Update 12A set P6='{}' where day='wednesday'".format(l2[x19])) 
            x20=random.randint(0,6)
            c.execute("Update 12A set P7='{}' where day='wednesday'".format("CCA")) 
            x21=random.randint(0,6)
            c.execute("Update 12A set P8='{}' where day='wednesday'".format("CCA"))
            l3=["Phy","Math","Chem","Eng","Bio/CS","Bio/CS PR","Game"] 
            x22=random.randint(0,6)
            c.execute("Update 12A set P2='{}' where day='thursday'".format(l3[x22])) 
            x23=random.randint(0,6)
            c.execute("Update 12A set P3='{}' where day='thursday'".format(l3[x23])) 
            x24=random.randint(0,6)
            c.execute("Update 12A set P4='{}' where day='thursday'".format(l3[x24])) 
            x25=random.randint(0,6)
            
            c.execute("Update 12A set P5='{}' where day='thursday'".format(l3[x25])) 
            x26=random.randint(0,6)
            c.execute("Update 12A set P6='{}' where day='thursday'".format(l3[x26])) 
            x27=random.randint(0,6)
            c.execute("Update 12A set P7='{}' where day='thursday'".format(l3[x27])) 
            x28=random.randint(0,6)
            c.execute("Update 12A set P8='{}' where day='thursday'".format(l3[x28]))

            l4=["Phy","Math","Chem","Eng","Bio/CS","G & C"] 
            x29=random.randint(0,5)
            c.execute("Update 12A set P2='{}' where day='friday'".format(l4[x29])) 
            x30=random.randint(0,5)
            c.execute("Update 12A set P3='{}' where day='friday'".format(l4[x30])) 
            x31=random.randint(0,5)
            c.execute("Update 12A set P4='{}' where day='friday'".format(l4[x31])) 
            x32=random.randint(0,5)
            c.execute("Update 12A set P5='{}' where day='friday'".format(l4[x32])) 
            x33=random.randint(0,5)
            c.execute("Update 12A set P6='{}' where day='friday'".format(l4[x33])) 
            x34=random.randint(0,5)
            c.execute("Update 12A set P7='{}' where day='friday'".format(l4[x34])) 
            x35=random.randint(0,5)
            c.execute("Update 12A set P8='{}' where day='friday'".format(l4[x35]))
            l5=["Phy","Math","Chem","Eng","Bio/CS"]
            x36=random.randint(0,4)
            c.execute("Update 12A set P2='{}' where day='saturday'".format(l5[x36])) 
            x37=random.randint(0,4)
            c.execute("Update 12A set P3='{}' where day='saturday'".format(l5[x37])) 
            x38=random.randint(0,4)
            c.execute("Update 12A set P4='{}' where day='saturday'".format(l5[x38])) 
            x39=random.randint(0,4)
            c.execute("Update 12A set P5='{}' where day='saturday'".format(l5[x39])) 
            x40=random.randint(0,4)
            c.execute("Update 12A set P6='{}' where day='saturday'".format(l5[x40])) 
            x41=random.randint(0,4)
            c.execute("Update 12A set P7='{}' where day='saturday'".format(l5[x41])) 
            x42=random.randint(0,4)
            c.execute("Update 12A set P8='{}' where day='saturday'".format(l5[x42])) 
            d.commit()
            print("Generated") 
            print("	")

        elif cle==12 and sece in ("Bb"):
            d1=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c1=d1.cursor()
            m=["Phy","Math/Hindi","Chem","Eng","Phy/Chem PR"] 
            c1.execute("Update 12B set P1='{}' ".format("Bio"))
            
            y1=random.randint(0,4)
            c1.execute("Update 12B set P2='{}' where day='monday'".format(m[y1])) 
            y2=random.randint(0,4)
            c1.execute("Update 12B set P3='{}' where day='monday'".format(m[y2])) 
            y3=random.randint(0,4)
            c1.execute("Update 12B set P4='{}' where day='monday'".format(m[y3])) 
            y4=random.randint(0,4)
            c1.execute("Update 12B set P5='{}' where day='monday'".format(m[y4])) 
            y5=random.randint(0,4)
            c1.execute("Update 12B set P6='{}' where day='monday'".format(m[y5])) 
            y6=random.randint(0,4)
            c1.execute("Update 12B set P7='{}' where day='monday'".format(m[y6])) 
            y7=random.randint(0,4)
            c1.execute("Update 12B set P8='{}' where day='monday'".format(m[y7]))
            m1=["Phy","Math/Hindi","Chem","Eng"] 
            y8=random.randint(0,3)
            c1.execute("Update 12B set P2='{}' where day='tuesday'".format(m1[y8])) 
            y9=random.randint(0,3)
            c1.execute("Update 12B set P3='{}' where day='tuesday'".format(m1[y9])) 
            y10=random.randint(0,3)
            c1.execute("Update 12B set P4='{}' where day='tuesday'".format(m1[y10])) 
            y11=random.randint(0,3)
            c1.execute("Update 12B set P5='{}' where day='tuesday'".format(m1[y11])) 
            y12=random.randint(0,3)
            c1.execute("Update 12B set P6='{}' where day='tuesday'".format(m1[y12])) 
            y13=random.randint(0,3)
            c1.execute("Update 12B set P7='{}' where day='tuesday'".format(m1[y13])) 
            y14=random.randint(0,3)
            c1.execute("Update 12B set P8='{}' where day='tuesday'".format(m1[y14]))
            m2=["Phy","Math/Hindi","Chem","Eng","Bio","PHE/PAI","Lib"] 
            y15=random.randint(0,6)
            c1.execute("Update 12B set P2='{}' where day='wednesday'".format(m2[y15])) 
            y16=random.randint(0,6)
            c1.execute("Update 12B set P3='{}' where day='wednesday'".format(m2[y16])) 
            y17=random.randint(0,6)
            c1.execute("Update 12B set P4='{}' where day='wednesday'".format(m2[y17])) 
            y18=random.randint(0,6)
            c1.execute("Update 12B set P5='{}' where day='wednesday'".format(m2[y18])) 
            y19=random.randint(0,6)
            c1.execute("Update 12B set P6='{}' where day='wednesday'".format(m2[y19])) 
            y20=random.randint(0,6)
            c1.execute("Update 12B set P7='{}' where day='wednesday'".format(m2[y20])) 
            y21=random.randint(0,6)
            c1.execute("Update 12B set P8='{}' where day='wednesday'".format(m2[y21]))

            m3=["Phy","Math/Hindi","Chem","Eng","Bio PR","Bio PR","Game"] 
            y22=random.randint(0,6)
            
            c1.execute("Update 12B set P2='{}' where day='thursday'".format(m3[y22])) 
            y23=random.randint(0,6)
            c1.execute("Update 12B set P3='{}' where day='thursday'".format(m3[y23])) 
            y24=random.randint(0,6)
            c1.execute("Update 12B set P4='{}' where day='thursday'".format(m3[y24])) 
            y25=random.randint(0,6)
            c1.execute("Update 12B set P5='{}' where day='thursday'".format(m3[y25])) 
            y26=random.randint(0,6)
            c1.execute("Update 12B set P6='{}' where day='thursday'".format(m3[y26])) 
            y27=random.randint(0,6)
            c1.execute("Update 12B set P7='{}' where day='thursday'".format(m3[y27])) 
            y28=random.randint(0,6)
            c1.execute("Update 12B set P8='{}' where day='thursday'".format(m3[y28]))


            m4=["Phy","Math/Hindi","Chem","Eng","Bio","G & C"] 
            y29=random.randint(0,5)
            c1.execute("Update 12B set P2='{}' where day='friday'".format(m4[y29])) 
            y30=random.randint(0,5)
            c1.execute("Update 12B set P3='{}' where day='friday'".format(m4[y30])) 
            y31=random.randint(0,5)
            c1.execute("Update 12B set P4='{}' where day='friday'".format(m4[y31])) 
            y32=random.randint(0,5)
            c1.execute("Update 12B set P5='{}' where day='friday'".format(m4[y32])) 
            y33=random.randint(0,5)
            c1.execute("Update 12B set P6='{}' where day='friday'".format(m4[y33])) 
            y34=random.randint(0,5)
            c1.execute("Update 12B set P7='{}' where day='friday'".format(m4[y34])) 
            y35=random.randint(0,5)
            c1.execute("Update 12B set P8='{}' where day='friday'".format(m[y35]))
            m5=["Phy","Math/Hindi","Chem","Eng","Bio"] 
            y36=random.randint(0,4)
            c1.execute("Update 12B set P2='{}' where day='saturday'".format(m5[y36])) 
            y37=random.randint(0,4)
            c1.execute("Update 12B set P3='{}' where day='saturday'".format(m5[y37])) 
            y38=random.randint(0,4)
            c1.execute("Update 12B set P4='{}' where day='saturday'".format(m5[y38])) 
            y39=random.randint(0,4)
            c1.execute("Update 12B set P5='{}' where day='saturday'".format(m5[y39])) 
            y40=random.randint(0,4)
            c1.execute("Update 12B set P6='{}' where day='saturday'".format(m5[y40])) 
            y41=random.randint(0,4)
            c1.execute("Update 12B set P7='{}' where day='saturday'".format(m5[y41])) 
            y42=random.randint(0,4)
            c1.execute("Update 12B set P8='{}' where day='saturday'".format(m5[y42]))
            d1.commit()
            print("Generated") 
            print("	")

        elif cle==12 and sece in ("cC"):
            d2=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c2=d2.cursor()
            c2.execute("Update 12C set P1='{}' ".format("Eco"))
            n=["Hist","Geo","Eng","Math/Hindi","PHE/PAI","Lib","Eco"] 
            z1=random.randint(0,6)
            c2.execute("Update 12C set P2='{}' where day='tuesday'".format(n[z1])) 
            z2=random.randint(0,6)
            c2.execute("Update 12C set P3='{}' where day='tuesday'".format(n[z2])) 
            z3=random.randint(0,6)
            c2.execute("Update 12C set P4='{}' where day='tuesday'".format(n[z3])) 
            z4=random.randint(0,6)
            c2.execute("Update 12C set P5='{}' where day='tuesday'".format(n[z4])) 
            z5=random.randint(0,6)
            c2.execute("Update 12C set P6='{}' where day='tuesday'".format(n[z5])) 
            z6=random.randint(0,6)
            c2.execute("Update 12C set P7='{}' where day='tuesday'".format(n[z6])) 
            z7=random.randint(0,6)
            c2.execute("Update 12C set P8='{}' where day='tuesday'".format(n[z7]))
            n1=["Hist","Geo","Eco","Eng","Math/Hindi"]
            z8=random.randint(0,4)
            c2.execute("Update 12C set P2='{}' where day='wednesday'".format(n1[z8])) 
            z9=random.randint(0,4)
            c2.execute("Update 12C set P3='{}' where day='wednesday'".format(n1[z9]))
            z10=random.randint(0,4)
            c2.execute("Update 12C set P4='{}' where day='wednesday'".format(n1[z10])) 
            z11=random.randint(0,4)
            c2.execute("Update 12C set P5='{}' where day='wednesday'".format(n1[z11])) 
            z12=random.randint(0,4)
            c2.execute("Update 12C set P6='{}' where day='wednesday'".format(n1[z12])) 
            z13=random.randint(0,4)
            c2.execute("Update 12C set P7='{}' where day='wednesday'".format("CCA"))
            z14=random.randint(0,4)
            c2.execute("Update 12C set P8='{}' where day='wednesday'".format("CCA"))
            n2=["Hist","Geo","Eco","Eng","Math/Hindi","G & C"] 
            z15=random.randint(0,5)
            c2.execute("Update 12C set P2='{}' where day='thursday'".format(n2[z15])) 
            z16=random.randint(0,5)
            c2.execute("Update 12C set P3='{}' where day='thursday'".format(n2[z16])) 
            z17=random.randint(0,5)
            c2.execute("Update 12C set P4='{}' where day='thursday'".format(n2[z17])) 
            z18=random.randint(0,5)
            c2.execute("Update 12C set P5='{}' where day='thursday'".format(n2[z18])) 
            z19=random.randint(0,5)
            c2.execute("Update 12C set P6='{}' where day='thursday'".format(n2[z19])) 
            z20=random.randint(0,5)
            
            c2.execute("Update 12C set P7='{}' where day='thursday'".format(n2[z20])) 
            z21=random.randint(0,5)
            c2.execute("Update 12C set P8='{}' where day='thursday'".format(n2[z21]))

            n3=["Hist","Geo","Eng","Math/Hindi","Eco PR","Eco PR"]
            z22=random.randint(0,5)
            c2.execute("Update 12C set P2='{}' where day='friday'".format(n3[z22])) 
            z23=random.randint(0,5)
            c2.execute("Update 12C set P3='{}' where day='friday'".format(n3[z23])) 
            z24=random.randint(0,5)
            c2.execute("Update 12C set P4='{}' where day='friday'".format(n3[z24]))
            z25=random.randint(0,5)
            c2.execute("Update 12C set P5='{}' where day='friday'".format(n3[z25]))
            z26=random.randint(0,5)
            c2.execute("Update 12C set P6='{}' where day='friday'".format(n3[z26])) 
            z27=random.randint(0,5)
            c2.execute("Update 12C set P7='{}' where day='friday'".format(n3[z27])) 
            z28=random.randint(0,5)
            c2.execute("Update 12C set P8='{}' where day='friday'".format(n3[z28]))

            n4=["Hist","Geo","Eco","Eng","Math/Hindi"] 
            z29=random.randint(0,4)
            c2.execute("Update 12C set P2='{}' where day='saturday'".format(n4[z29])) 
            z30=random.randint(0,4)
            c2.execute("Update 12C set P3='{}' where day='saturday'".format(n4[z30])) 
            z31=random.randint(0,4)
            c2.execute("Update 12C set P4='{}' where day='saturday'".format(n4[z31])) 
            z32=random.randint(0,4)
            c2.execute("Update 12C set P5='{}' where day='saturday'".format(n4[z32]))
            z33=random.randint(0,4)
            c2.execute("Update 12C set P6='{}' where day='saturday'".format(n4[z33])) 
            z34=random.randint(0,4)
            c2.execute("Update 12C set P7='{}' where day='saturday'".format(n4[z34])) 
            z35=random.randint(0,4)
            c2.execute("Update 12C set P8='{}' where day='saturday'".format(n4[z35]))

            n5=["Hist","Geo","Eng","Math/Hindi","Game","Math/Hindi"] 
            z36=random.randint(0,5)
            c2.execute("Update 12C set P2='{}' where day='monday'".format(n5[z36])) 
            z37=random.randint(0,5)
            c2.execute("Update 12C set P3='{}' where day='monday'".format(n5[z37])) 
            z38=random.randint(0,5)
            c2.execute("Update 12C set P4='{}' where day='monday'".format(n5[z38])) 
            z39=random.randint(0,5)
            c2.execute("Update 12C set P5='{}' where day='monday'".format(n5[z39])) 
            z40=random.randint(0,5)
            c2.execute("Update 12C set P6='{}' where day='monday'".format(n5[z40])) 
            z41=random.randint(0,5)
            c2.execute("Update 12C set P7='{}' where day='monday'".format(n5[z41])) 
            z42=random.randint(0,5)
            
            c2.execute("Update 12C set P8='{}' where day='monday'".format(n5[z42])) 
            d2.commit()
            print("Generated") 
            print("	")
        else:
            print("Entered class doesn't exist in our database")
    if b==1:
        AddTeacher()
    elif b==2: 
        DelTeacher()

    elif b==3: 
        AddClass()
    elif b==4: 
        DelClass()
    elif b==5: 
        GenTT()
    else:
        print("Enter a valid number") 
        print("	")

def student():
    print("----Student Menu	")
    print("1.Select class to view timetable") 
    print("2.View subjectwise timetable") 
    print("3.View practical classes") 
    print("4.View theory classes") 
    print("Enter any number to go back")
    f=int(input("Enter what you want to do:- "))

    def ViewTT():
        try:
            ec=input("Enter your class:- ") 
            scv=input("Enter section:- ") 
            escv=ec+scv
            d3=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c3=d3.cursor()


            c3.execute("select * from {}".format(escv))
            tt=c3.fetchall()
            print("DAY/Period","-"*5,"P1","-"*13,"P2","-"*13,"P3","-"*13,"P4","-"*13,"P5","-"*13,"P6","-"*13,"P7","-"*13,"P8")
            for i in tt: 
                l10=len(i[0])
                l11=len(i[1])
                l12=len(i[2])
                l13=len(i[3])
                l14=len(i[4])
                l15=len(i[5])
                l16=len(i[6])
                l17=len(i[7])
                l18=len(i[8])
                print(i[0],"-"*(15-l10),i[1],"-"*(15-l11),i[2],"-"*(15-l12),i[3],"-"*(15-l13),i[4],"-"*(15-l14),i[5],"-"*(15-l15),i[6],"-"*(15-l16),i[7],"-"*(15-l17),i[8])

            d3.commit() 
        except:
            print("Either entered class/section doesn't exist or") 
            print("Recheck and enter appropriate values")
        print("	")
    def SubTT():
        try:
            ecd=input("Enter your class:- ") 
            scd=input("Enter your section:- ") 
            escd=ecd+scd
            print("Abbreviations used","-"*2,"Subject") 
            print("Phy","-"*17,"Physics")
            print("Chem","-"*16,"Chemistry")
            print("Math","-"*16,"Mathematics")
            print("Eng","-"*17,"English")
            print("Bio/CS--for 12a","-"*6,"Biology/Computer Science") 
            print("PHE/PAI","-"*13,"Physical Education/Painting") 
            print("Lib","-"*17,"Library")
            print("G & C","-"*15,"Counselling and guidance") 
            print("Math/Hindi--for 12b,12c","-"*1,"Mathematics/Hindi") 
            print("Bio--for 12b","-"*9,"Biology")
            print("CCA","-"*17,"Co-curricular Activities") 
            print("Phy/Chem PR","-"*9,"Physics/Chemistry Practical")
            print("Bio/CS PR","-"*11,"Biology/Computer Science Practical") 
            print("Eco","-"*17,"Economics")
            print("Hist","-"*16,"History")
            print("Geo","-"*17,"Geography")
            print("Eco PR","-"*14,"Economics Practical") 
            subd=input("Enter subject:- ")
            d8=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c8=d8.cursor()
            c8.execute("select day from {} where P1 like '%{}%' ;".format(escd,subd)) 
            pr1=c8.fetchall()
            pl1=len(pr1)
            for i in range (1): 
                for j in pr1:
                    print("P1",j[0])
            c8.execute("select day from {} where P2 like '%{}%' ;".format(escd,subd)) 
            pr2=c8.fetchall()
            pl2=len(pr2)
            
            for i in range (1): 
                for j in pr2:
                    print("P2",j[0])
            c8.execute("select day from {} where P3 like '%{}%' ;".format(escd,subd)) 
            pr3=c8.fetchall()
            pl3=len(pr3)
            for i in range (1): 
                for j in pr3:
                    print("P3",j[0])
            c8.execute("select day from {} where P4 like '%{}%' ;".format(escd,subd)) 
            pr4=c8.fetchall()
            pl4=len(pr4)
            for i in range (1): 
                for j in pr4:
                    print("P4",j[0])
            c8.execute("select day from {} where P5 like '%{}%' ;".format(escd,subd)) 
            pr5=c8.fetchall()
            pl5=len(pr5)
            for i in range (1): 
                for j in pr5:
                    print("P5",j[0])
            c8.execute("select day from {} where P6 like '%{}%' ;".format(escd,subd)) 
            pr6=c8.fetchall()
            pl6=len(pr6)
            for i in range (1): 
                for j in pr6:
                    print("P6",j[0])
            c8.execute("select day from {} where P7 like '%{}%' ;".format(escd,subd)) 
            pr7=c8.fetchall()
            pl7=len(pr7)
            for i in range (1): 
                for j in pr7:
                    print("P7",j[0])
            c8.execute("select day from {} where P8 like '%{}%' ;".format(escd,subd)) 
            pr8=c8.fetchall()
            pl8=len(pr8)
            for i in range (1): 
                for j in pr8:
                    print("P8",j[0])

        except:
            print("Enter appropriate values")

    def PrTT():
        try:
            ecf=input("Enter your class- ") 
            scf=input("Enter your section:- ") 
            escf=ecf+scf
            
            d9=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c9=d9.cursor()
            c9.execute("select day,P1 from {} where P1 like '%PR%' ;".format(escf)) 
            pr17=c9.fetchall()
            pl17=len(pr17) 
            for i in range (1):
                for j in pr17: 
                    print("P8",j[0],j[1])
            c9.execute("select day,P2 from {} where P2 like '%PR%' ;".format(escf)) 
            pr18=c9.fetchall()
            pl18=len(pr18) 
            for i in range (1):
                for j in pr18: 
                    print("P8",j[0],j[1])
            c9.execute("select day,P3 from {} where P3 like '%PR%' ;".format(escf)) 
            pr19=c9.fetchall()
            pl19=len(pr19) 
            for i in range (1):
                for j in pr19: 
                    print("P8",j[0],j[1])
            c9.execute("select day,P4 from {} where P4 like '%PR%' ;".format(escf)) 
            pr20=c9.fetchall()
            pl20=len(pr20) 
            for i in range (1):
                for j in pr20: 
                    print("P8",j[0],j[1])
            c9.execute("select day,P5 from {} where P5 like '%PR%' ;".format(escf)) 
            pr21=c9.fetchall()
            pl21=len(pr21) 
            for i in range (1):
                for j in pr21: 
                    print("P8",j[0],j[1])
            c9.execute("select day,P6 from {} where P6 like '%PR%' ;".format(escf)) 
            pr22=c9.fetchall()
            pl22=len(pr22) 
            for i in range (1):
                for j in pr22: 
                    print("P8",j[0],j[1])
            c9.execute("select day,P7 from {} where P7 like '%PR%' ;".format(escf)) 
            pr23=c9.fetchall()
            pl23=len(pr23) 
            for i in range (1):
                for j in pr23: 
                    print("P8",j[0],j[1])
            c9.execute("select day,P8 from {} where P8 like '%PR%' ;".format(escf)) 
            pr24=c9.fetchall()
            pl24=len(pr24) 
            for i in range (1):
                for j in pr24: 
                    print("P8",j[0],j[1])
            
        except:
            print("Enter appropriate values")

    def ThTT():
        try:
            ece=input("Enter your class:- ") 
            sce=input("Enter your section:- ") 
            esce=ece+sce
            print("Abbreviations used","-"*2,"Subject") 
            print("Phy","-"*17,"Physics")
            print("Chem","-"*16,"Chemistry")
            print("Math","-"*16,"Mathematics")
            print("Eng","-"*17,"English")
            print("Bio/CS--for 12a","-"*6,"Biology/Computer Science") 
            print("PHE/PAI","-"*13,"Physical Education/Painting") 
            print("Lib","-"*17,"Library")
            print("G & C","-"*15,"Counselling and guidance") 
            print("Math/Hindi--for 12b,12c","-"*1,"Mathematics/Hindi") 
            print("Bio--for 12b","-"*9,"Biology")
            print("CCA","-"*17,"Co-curricular Activities") 
            print("Phy/Chem PR","-"*9,"Physics/Chemistry Practical")
            print("Bio/CS PR","-"*11,"Biology/Computer Science Practical") 
            print("Eco","-"*17,"Economics")
            print("Hist","-"*16,"History")
            print("Geo","-"*17,"Geography")
            print("Eco PR","-"*14,"Economics Practical") 
            sre=input("Enter subject:- ")
            d7=msc.connect(host="localhost",user="root",password="admin",database="Time_table_arrangement") 
            c7=d7.cursor()
            c7.execute("select day,P1 from {} where P1='{}' ;".format(esce,sre)) 
            pr9=c7.fetchall()
            pl9=len(pr9)
            for i in range (1): 
                for j in pr9:
                    print("P1",j[0],j[1])
            c7.execute("select day,P2 from {} where P2='{}';".format(esce,sre)) 
            pr10=c7.fetchall()
            pl10=len(pr10) 
            for i in range (1):
                for j in pr10: 
                    print("P2",j[0])
            c7.execute("select day,P3 from {} where P3='{}' ;".format(esce,sre)) 
            pr11=c7.fetchall()
            pl11=len(pr11) 
            for i in range (1):
                for j in pr11: 
                    print("P3",j[0])
            c7.execute("select day,P4 from {} where P4='{}' ;".format(esce,sre)) 
            pr12=c7.fetchall()
            
            pl12=len(pr12) 
            for i in range (1):
                for j in pr12: 
                    print("P4",j[0])
            c7.execute("select day,P5 from {} where P5='{}' ;".format(esce,sre)) 
            pr13=c7.fetchall()
            pl13=len(pr13) 
            for i in range (1):
                for j in pr13: 
                    print("P5",j[0])
            c7.execute("select day,P6 from {} where P6='{}';".format(esce,sre)) 
            pr14=c7.fetchall()
            pl14=len(pr14) 
            for i in range (1):
                for j in pr14: 
                    print("P6",j[0])
            c7.execute("select day,P7 from {} where P7='{}' ;".format(esce,sre)) 
            pr15=c7.fetchall()
            pl15=len(pr15) 
            for i in range (1):
                for j in pr15: 
                    print("P7",j[0])
            c7.execute("select day,P8 from {} where P8='{}' ;".format(esce,sre)) 
            pr16=c7.fetchall()
            pl16=len(pr16) 
            for i in range (1):
                for j in pr16: 
                    print("P8",j[0])
            print("	")
        except:
            print("Enter appropriate values")

    if f==1:
        ViewTT() 
    elif f==2:
        SubTT()
    elif f==3: 
        PrTT()
    elif f==4: 
        ThTT()
    elif f == 5:
        GenTT()
    else:
        print("Enter a valid no.") 
        print("	")

while True:
    print("----Welcome	")
    print("Enter 1 for Teacher") 
    print("Enter 2 for Student") 
    print("Enter 3 to Exit")

    try:
        a=int(input("Enter who you are:- ")) 
        if a==1:
            Teacher()

        elif a==2: 
            student()
        elif a==3:
            print("----Thank you")
            break 
    except:
        print("Enter appropriate values")




        








  
