 from datetime import date
import datetime
import time

d={}
ch=0
dt=datetime.datetime.today()
a=0
today=date.today()
d1={}
d2={}
dlt=''
d3={}
d4={}
d5={}
### Extras
passw='123'




###main code
while True:
 print("Hospital Management")
 print("Services offered : \n 1.Patient login \n 2.Admin login \n 3.Exit")
 ch=int(input("Enter choice : "))
 if ch==1:
     print("Welcome .....      You logged in at : ",dt)
     print("Services offered : \n 1.Book Appointment \n 2.See Bill Of Patient")
     try:    ###exception handling
         u=int(input("enter your choice: "))
         if u==1:
             print(" Enter 0 to exit  \n Enter 1 to continue")
             u1 = int(input("Enter your choice : "))
             if u1==1:
                 print("Select Date for Appointment : ")
                 nm=input("Enter Name Of Patient")
                 year=int(input("Enter Year : "))
                 month=int(input("Enter month : "))
                 day=int(input("Enter Day : "))
                 dtt=date(year,month,day)
                 d5[nm]=dtt
                 print(" Appointment Booked ! ")
             elif u1==0:
                 print("...")
                 break
             else:
                 print("Wrong Choice")
         elif u==2:
             biml=' .....INVOICE..... '
             print(biml.center(40))
             for i in d3:
                 print("\n Name of patient : ",i,"\n Bill Amount : ",d3[i])
                 for i in d1:
                     print("Other Information :","\n Age : ",i,"\n Reason of admit : ",d1[i])
             else:
                 print("Not Data Found")
         elif u==3:
             print("Thanks for using...  \n Logging Out...")
             break
         else:
             print("Wrong input")
     except:
         u = int(input("enter your choice: "))
         if u == 1:
             print(" Enter 0 to exit  \n Enter 1 to continue")
             u1 = int(input("Enter your choice : "))
             if u1 == 1:
                 print("Select Date for Appointment : ")
                 nm = input("Enter Name Of Patient")
                 year = int(input("Enter Year : "))
                 month = int(input("Enter month : "))
                 day = int(input("Enter Day : "))
                 dtt = date(year, month, day)
                 d5[nm] = dtt
                 print(" Appointment Booked ! ")
             elif u1 == 0:
                 print("...")
                 break
             else:
                 print("Wrong Choice")
         elif u == 2:
             biml = ' .....INVOICE..... '
             print(biml.center(40))
             for i in d3:
                 print("\n Name of patient : ", i, "\n Bill Amount : ", d3[i])
                 for i in d1:
                     print("Other Information :", "\n Age : ", i, "\n Reason of admit : ", d1[i])
             else:
                 print("Not Data Found")
         elif u == 3:
             print("Thanks for using...  \n Logging Out...")
             break
         else:
             print("Wrong input")
 elif ch==2:
        while True:
            pas=input("Enter Password")
            if pas==passw:
                print('='*69)
                print("Welcome Admin")
                print("Services ; \n 1.add new patient \n 2.search patient \n 3.delete patient \n 4.Make Bill of Patient \n 5.Logout")
                print('='*69)
            else:
                print("Wrong password")
            try: ## exception handling
                a=int(input("Enter your choice :"))
                if a==1:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1=int(input("Enter your choice : "))
                    if a1==1:
                        print("Enter Information of patient")
                        nm=input("Enter name of patient")
                        rsn=input("Enter Reason to Admit")
                        age=int(input("Enter age :"))
                        dtt=today
                        d[nm]=rsn
                        d1[age]=dtt
                        d.update(d2)
                        print("Processinng...")
                        time.sleep(3)
                        print("Done")
                    elif a1==0:
                        print("...")
                        break
                    else:
                        print("Enter Valid choice ...")
                elif a==2:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1 = int(input("Enter your choice : ")) 
                    if a1==1:
                        print("Enter Info to search")
                        for i in d :
                            print("Total Patient : ",len(d))
                            sr = input("Enter name of Patient :")
                            if sr==i:
                             print("\n Name :",i," \n Reason of Admit: ",d[i])
                             for i in d1:
                                 print(" Age : ",i,"\n Date Of Admit ",d1[i])
                            else:
                                print("Not Found")
                        else:
                            print("...")
                    elif a1==0:
                        print("...")
                        break
                    else:
                        print("Enter valid choice")
                elif a==3:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1 = int(input("Enter your choice : "))
                    if a1==1:
                        print("Information below : ")
                        for i in d:
                            print("Total Patient : ", len(d))
                            dlt = input("Enter name of Patient :")
                            if dlt == i:
                                print("Deleting...")
                                d.clear()
                                for i in d1:
                                    d1.clear()
                                    time.sleep(3)
                                print("Done...!")
                            else:
                                print("Not Data Found")
                        else:
                            print("No Data found")
                    elif a1==0:
                        print("....")
                    else:
                        print("Enter valid choice")
                elif a==4:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1 = int(input("Enter your choice : "))
                    if a1==1:
                        print("Bill information :")
                        b=input("Enter Name Of Patient")
                        bi=int(input("Enter Bill Amount"))
                        d3[b]=bi
                        h='Bill Generated'
                        print(h.center(50))
                        for i in d3:
                            print("\n Name of Patient :",i,"\n Total Ammount in rs :",d3[i])
                            print("Want to do any changes ? ")
                            er=input("press Y for yes , N for no : ")
                            if er=='y' or er=='Y':
                                print("Re enter information : ")
                                b = input("Enter Name Of Patient")
                                bi = int(input("Enter Bill Amount"))
                                d3[b]=bi
                                d4.update(d3)
                                h = 'Bill Generated'
                                print(h.center(50))
                                for i in d4:
                                    print("\n Name of Patient :", i, "\n Total Ammount in rs :", d4[i])
                                else:
                                    print(" Error ")
                            else:
                                break    
                        else:
                            print("Error")
                    elif a1==0:
                        print("...")
                        break
                elif a==5:
                    print("Logging out...")
                    time.sleep(3)
                    break
                else:
                    print("wrong choice")
            except:
                print("Please Enter Valid Options !")
                a = int(input("Enter your choice :"))
                if a == 1:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1 = int(input("Enter your choice : "))
                    if a1 == 1:
                        print("Enter Information of patient")
                        nm = input("Enter name of patient")
                        rsn = input("Enter Reason to Admit")
                        age = int(input("Enter age :"))
                        dtt = today
                        d[nm] = rsn
                        d1[age] = dtt
                        d.update(d2)
                        print( "Processinng...")
                        time.sleep(3)
                        print( "Done")
                    elif a1 == 0:
                        print("...")
                        break
                    else:
                        print("Enter Valid choice ...")
                elif a == 2:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1 = int(input("Enter your choice : "))
                    if a1 == 1:
                        print( "Enter Info to search")
                        for i in d:
                            print("Total Patient : ", len(d))
                            sr = input("Enter name of Patient :")
                            if sr == i:
                                print("\n Name :", i, " \n Reason of Admit: ", d[i])
                                for i in d1:
                                    print(" Age : ", i, "\n Date Of Admit ", d1[i])
                            else:
                                print("Not Found")
                        else:
                            print("...")
                    elif a1 == 0:
                        print("...")
                        break
                    else:
                        print("Enter valid choice")
                elif a == 3:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1 = int(input("Enter your choice : "))
                    if a1 == 1:
                        print("Information below : ")
                        for i in d:
                            print("Total Patient : ", len(d))
                            dlt = input("Enter name of Patient :")
                            if dlt == i:
                                print("Deleting...")
                                d.clear()
                                for i in d1:
                                    d1.clear()
                                    time.sleep(3)
                                print("Done...!")
                            else:
                                print("Not Data Found")
                        else:
                            print("No Data found")
                    elif a1 == 0:
                        print("....")
                    else:
                        print("Enter valid choice")
                elif a == 4:
                    print(" Enter 0 to exit  \n Enter 1 to continue")
                    a1 = int(input("Enter your choice : "))
                    if a1 == 1:
                        print("Bill information :")
                        b = input("Enter Name Of Patient")
                        bi = int(input("Enter Bill Amount"))
                        d3[b] = bi
                        h = 'Bill Generated'
                        print(h.center(50))
                        for i in d3:
                            print("\n Name of Patient :", i, "\n Total Ammount in rs :", d3[i])
                            print("Want to do any changes ? ")
                            er = input("press Y for yes , N for no : ")
                            if er == 'y' or er == 'Y':
                                print("Re enter information : ")
                                b = input("Enter Name Of Patient")
                                bi = int(input("Enter Bill Amount"))
                                d3[b] = bi
                                d4.update(d3)
                                h = 'Bill Generated'
                                print(h.center(50))
                                for i in d4:
                                    print("\n Name of Patient :", i, "\n Total Ammount in rs :", d4[i])
                                else:
                                    print(" Error ")
                            else:
                                break
                        else:
                            print("Error")
                elif a == 5:
                    print("Logging out...")
                    time.sleep(3)
                    break
                else:
                    print("wrong choice")

 elif ch==3:
     print("Thanks For using...")
     exit()
