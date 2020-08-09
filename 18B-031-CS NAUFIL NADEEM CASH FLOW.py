from abc import ABC, abstractmethod
from tkinter import*
import tkinter as tk
from tkinter import messagebox
import sqlite3
#import matplotlib.pyplot as plt
con=sqlite3.connect('Cash Flow.db')
c=con.cursor()



class Departmental_Store():
    def __init__(self):
        self.con=sqlite3.connect('Cash Flow.db')
        self.c= self.con.cursor()
        self.date=None
        self.Prod_name=None
        self.No_of_prod=None



class Recorded_Data(Departmental_Store,ABC):
    
    def Create_Table(self): 
         c.execute('CREATE TABLE IF NOT EXISTS Hyper_Mart_Record(DATE integer,Name_of_Product Text,No_of_Product integer,Total integer,Net_Income integer)')
         con= sqlite3.connect('Cash Flow.db')
         cur=con.cursor()





class Revenue(Recorded_Data):
    
   
    def MainScreen(self):
        screen=Tk()
        screen.geometry("300x300")
        screen.title("MAIN MENU")
        heading= Label(screen,text="MAIN MENU",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12,'bold'))
        heading.pack()
        heading1= Label(screen,text="Cash Flow System",bg="black",fg="white",width="300",height="3",font=("Lucida Console",12,'bold'))
        heading1.pack()
        def leftClick(event):
            screen.destroy()
            self.Cal()
        Entry_button=Button(screen,text="Enter Entry", width="100", height="3",font=("Lucida Console",12))
        Entry_button.pack()
        Entry_button.bind('<Button-1>',leftClick)
        def RighClick(event):
                screen.destroy()
        quit_button= Button(screen,font=('arial',8,'bold'),text="QUIT",bg="black",fg="white" )
        quit_button.place(x=255,y=270)
        quit_button.bind('<Button-1>', RighClick)

        
   
    def Cal(self):
        screen2 = Tk()
        screen2.geometry("300x300")
        screen2.title("Inventory Entries of Today sale")
        heading= Label(screen2,text="Today Sale Inventory",bg="black",fg="white",width="500",height="3",font=("Lucida Console",12))
        heading.pack()


        Date = Label(screen2,text="Enter Date")
        Product_Name= Label(screen2,text="Enter Product Name")

        Date.place(x=50, y=70)
        Product_Name.place(x=50 , y=150)

        self.Date =  StringVar()
        self.Date = Entry(screen2,textvariable =Date, width="30")
        self.Product_Name=StringVar()
        self.Product_Name = Entry(screen2,textvariable =Product_Name, width="30")
            

        self.Date.place(x=50, y=100)
        self.Product_Name.place(x=50,y=180)

        def leftClick(event):
            

            screen3=Tk()
            screen3.geometry("300x200")
            screen2.title("Inventory Entries of Today sale")
            heading= Label(screen3,text="Today Sale Inventory",bg="black",fg="white",width="500",height="3",font=("Lucida Console",12))
            heading.pack()



            Prod_NO= Label(screen3,text="Enter Number of Product Sale Today")
            Prod_NO.place(x=50 , y=70)

           
            self.Prod_No= Entry(screen3,textvariable =Prod_NO, width="30")
            self.Prod_No.place(x=50, y=100)
            def leftClick(event):
                def save(Date,Product_Name):
                    self.date=self.Date.get()
                    self.Prod_name=self.Product_Name.get()
                    self.No_of_prod=self.Prod_No.get()
                    
               
                save(Date,Product_Name)
                dictt={'fragnance':50,'rice':60,'oil':70,"beans":120,"flour":80,"sugar":80,"butter":180}
                if self.Prod_name in dictt:
                    for key,value in dictt.items():
                        self.total=int(value)*int(self.No_of_prod)
                else:
                     messagebox.showinfo('Product not Found')
                
               
                con=sqlite3.connect('Cash Flow.db')
                c=con.cursor()
                cur = con.cursor()
                c.execute("Insert into Hyper_Mart_Record (DATE ,Name_of_Product ,No_of_Product,Total ) values (?,?,?,?)", (self.date,self.Prod_name,self.No_of_prod,self.total))
                con.commit()
                con=sqlite3.connect('Cash Flow.db')
                c=con.cursor()
                cur = con.cursor()
                cur.execute("SELECT * FROM  Hyper_Mart_Record ")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
                Income.Income_Statement(self)
                screen2.destroy()
                screen3.destroy()
                    
            Submit_button= Button(screen3,font=('arial',8,'bold'),text="Submit",bg="black",fg="white" )
            Submit_button.place(x=240,y=155)
            Submit_button.bind('<Button-1>', leftClick)

                

            
        Submit_button= Button(screen2,font=('arial',8,'bold'),text="Submit",bg="black",fg="white" )
        Submit_button.place(x=240,y=270)
        Submit_button.bind('<Button-1>', leftClick)
class Income(Revenue):
    def Income_Statement(self):
        con= sqlite3.connect('Cash Flow.db')
        cur=con.cursor()
        cur.execute("SELECT SUM (Total) FROM Hyper_Mart_Record")
        a=cur.fetchall()
        print("-"*155)
        print("The Total Sale of Month:",a)
        cur.execute("Insert into Hyper_Mart_Record(Net_Income)values(?)",((a[0])))
        con.commit()
        print("-"*155)
        for i in a[0]:
            l=a[0]
        for j in l:
            if j < 50000:
                loss=50000-j
                print("Bussiness Monthly Loss is:",loss)
            else:
                loss=j-50000
                print("Bussiness Monthly Profit:",loss)
        

                
            
           
r=Recorded_Data()
r.Create_Table()
a=Revenue()
a.MainScreen()


con.commit()
c.close()
con.close()





