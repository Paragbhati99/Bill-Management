from tkinter import*

root=Tk()
root.geometry("1100x600")
root.title("Bill Management")
root.resizable(False,False)


def Reset():
    entry_Dosa.delete(0,END)
    entry_Cookies.delete(0,END)
    entry_Tea.delete(0,END)
    entry_Coffee.delete(0,END)
    entry_Juice.delete(0,END)
    entry_Pancakes.delete(0,END)
    entry_Eggs.delete(0,END)
    entry_VadaPav.delete(0,END)
    entry_Samosa.delete(0,END)
    
def Total():
     try:a1=int(Dosa.get()) 
     except: a1=0       
    
     try:a2=int(Cookies.get()) 
     except: a2=0    
    
     try:a3=int(Tea.get()) 
     except: a3=0    
    
     try:a4=int(Coffee.get()) 
     except: a4=0      
    
     try:a5=int(Juice.get()) 
     except: a5=0    
   
     try:a6=int(Pancakes.get()) 
     except: a6=0    
      
     try:a7=int(Eggs.get()) 
     except: a7=0    
   
     try:a8=int(VadaPav.get()) 
     except: a8=0    
   
     try:a9=int(Samosa.get()) 
     except: a9=0    
 
 #Define cost of each item per quantity
 
     c1=60*a1
     c2=30*a2
     c3=8*a3
     c4=30*a4
     c5=50*a5
     c6=15*a6
     c7=20*a7
     c8=50*a8
     c9=12*a9

     lbl_total=Label(f2,font=("aria",20,'bold'),text="Total", width=16, fg="lightyellow", bg="black")
     lbl_total.place(x=0,y=50)

     entry_total=Entry(f2,font=("aria",20,'bold'), textvariable=Total_bill, bd=6, width=15, bg="lightgreen")
     entry_total.place(x=20,y=100)
 
     totalcost=c1+c2+c3+c4+c5+c6+c7+c8+c9
     string_bill="Rs.",str('%.2f' %totalcost)
     Total_bill.set(string_bill)


Label(text="Bill Managenet", bg="black", fg="white", font=("calibiri",33), width="300", height="2").pack()

#Menu Card

f=Frame(root,bg="lightgreen", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10,y=118)

Label(f,text="Menu", font=("Gabriola", 40, "bold"),fg="black", bg= "lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Dosa...............Rs.60/Plate",fg="black", bg= "lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Cookies............Rs.30/Plate",fg="black", bg= "lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Tea................Rs.8/cup",fg="black", bg= "lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Coffee.............Rs.30/cup",fg="black", bg= "lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Juice..............Rs.50/cup",fg="black", bg= "lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Pancakes...........Rs.15/Piece",fg="black", bg= "lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Eggs...............Rs.10/Plate",fg="black", bg= "lightgreen").place(x=10,y=260)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Vada Pav...........Rs.50/Plate",fg="black", bg= "lightgreen").place(x=10,y=290)
Label(f,font=("Lucida Calligraphy", 15, "bold"), text="Samose.............Rs.12/Plate",fg="black", bg= "lightgreen").place(x=10,y=320)

#Entry Work
f1=Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()

Dosa=StringVar()
Cookies=StringVar()
Tea=StringVar()
Coffee=StringVar()
Juice=StringVar()
Pancakes=StringVar()
Eggs=StringVar()
VadaPav=StringVar()
Samosa=StringVar()
Total_bill=StringVar()


#Label

lbl_Dosa=Label(f1,font=("aria",20,"bold"),text="Dosa",width=12,fg="blue4",background="yellow")
lbl_Cookies=Label(f1,font=("aria",20,"bold"),text="Cookies",width=12,fg="blue4",background="yellow")
lbl_Tea=Label(f1,font=("aria",20,"bold"),text="Tea",width=12,fg="blue4",background="yellow")
lbl_Coffee=Label(f1,font=("aria",20,"bold"),text="Coffee",width=12,fg="blue4",background="yellow")
lbl_Juice=Label(f1,font=("aria",20,"bold"),text="Juice",width=12,fg="blue4",background="yellow")
lbl_Pancakes=Label(f1,font=("aria",20,"bold"),text="Pancakes",width=12,fg="blue4",background="yellow")
lbl_Eggs=Label(f1,font=("aria",20,"bold"),text="Eggs",width=12,fg="blue4",background="yellow")
lbl_VadaPav=Label(f1,font=("aria",20,"bold"),text="Vada Pav",width=12,fg="blue4",background="yellow")
lbl_Samosa=Label(f1,font=("aria",20,"bold"),text="Samosa",width=12,fg="blue4",background="yellow")

lbl_Dosa.grid(row=1,column=0)
lbl_Cookies.grid(row=2,column=0)
lbl_Tea.grid(row=3,column=0)
lbl_Coffee.grid(row=4,column=0)
lbl_Juice.grid(row=5,column=0)
lbl_Pancakes.grid(row=6,column=0)
lbl_Eggs.grid(row=7,column=0)
lbl_VadaPav.grid(row=8,column=0)
lbl_Samosa.grid(row=9,column=0)

#BILL
f2=Frame(root, bg="lightyellow", highlightbackground="Black", highlightthickness=1, width=300, height=400)
f2.place(x=790,y=122)

Bill=Label(f2,text="Bill",font=("calibiri",25),bg="lightyellow")
Bill.place(x=120,y=10)


#Entry 

entry_Dosa=Entry(f1,font=("aria",20,"bold"),textvariable="Dosa", bd=5, width=8,bg="lightpink")
entry_Cookies=Entry(f1,font=("aria",20,"bold"),textvariable="Cookies", bd=5, width=8,bg="lightpink")
entry_Tea=Entry(f1,font=("aria",20,"bold"),textvariable="Tea", bd=5, width=8,bg="lightpink")
entry_Coffee=Entry(f1,font=("aria",20,"bold"),textvariable="Coffee", bd=5, width=8,bg="lightpink")
entry_Juice=Entry(f1,font=("aria",20,"bold"),textvariable="Juice", bd=5, width=8,bg="lightpink")
entry_Pancakes=Entry(f1,font=("aria",20,"bold"),textvariable="Pancakes", bd=5, width=8,bg="lightpink")
entry_Eggs=Entry(f1,font=("aria",20,"bold"),textvariable="Eggs", bd=5, width=8,bg="lightpink")
entry_VadaPav=Entry(f1,font=("aria",20,"bold"),textvariable="VadaPav", bd=5, width=8,bg="lightpink")
entry_Samosa=Entry(f1,font=("aria",20,"bold"),textvariable="Samosa", bd=4, width=8,bg="lightpink")

entry_Dosa.grid(row=1,column=1)
entry_Cookies.grid(row=2,column=1)
entry_Tea.grid(row=3,column=1)
entry_Coffee.grid(row=4,column=1)
entry_Juice.grid(row=5,column=1)
entry_Pancakes.grid(row=6,column=1)
entry_Eggs.grid(row=7,column=1)
entry_VadaPav.grid(row=8,column=1)
entry_Samosa.grid(row=9,column=1)


#Buttons

btn_reset=Button(f1,bd=5,fg="black", bg="lightblue",font=("ariel",16,"bold"),width=10,text="Reset",command=Reset)
btn_reset.grid(row=10,column=0)

btn_total=Button(f1,bd=5,fg="Black",bg='lightblue', font=("ariel",16,"bold"),width=10,text="Total",command=Total)
btn_total.grid(row=10,column=1)


root.mainloop()


