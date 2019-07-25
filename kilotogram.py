from tkinter import *

window=Tk()

def from_kg():
    t1.insert(END,float(e1_value.get())*1000)
    t2.insert(END,float(e1_value.get())*2.20462)
    t3.insert(END,float(e1_value.get())*35.274)
    
b1=Button(window,text="convert",command=from_kg)
b1.grid(row=0,column=2)

e0=Label(window,text="kilos")
e0.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)


window.mainloop()
