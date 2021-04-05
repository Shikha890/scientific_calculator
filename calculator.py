from tkinter import Tk, Label ,Button,Frame,StringVar,Entry , messagebox

def clear():
    text_var.set("")
def square(y):
        return y**2
def pow(x,y):
        return x**y
    
def sqrt(y):
        return y**(0.5)
def percent(y,z):
        return (y/z)*100

def action(item):
    
    expression=text_var.get()+str(item)
    text_var.set(expression)

def equals():
     try:
        expression=text_var.get()
        result=round(float(eval(expression)),5)
        text_var.set(result)
    
     except ZeroDivisionError :
             text_var.set("zero_div_err:")
     
     except:
             text_var.set("invalid operation")
def sqr_root():
        
        expression=float(text_var.get())
        
        text_var.set(f"sqrt({expression})")
        
def backspace():
    expression=text_var.get()
    text_var.set(expression[:-1])   

def power():
    expression=float(text_var.get())
    
    expression=str(f'pow({expression},power )')
    text_var.set(expression)
def square_show():
        expression=float(text_var.get())
        text_var.set(f"square({expression})")
def percentage():
    expression=text_var.get()
    expression=str(f"percent({expression},principal)")

    text_var.set(expression)

root=Tk()

from platform import system
if system()=='Linux':
        root.geometry("312x440")
        messagebox.showinfo('INFORMATION','hey so are using linux good')
        wid=6
        
elif system()=='Windows':
        messagebox.showinfo('INFORMATION','hey so are using windows some \
of the features might not work correctly')

        root.geometry("240x380")
        wid=7
root.resizable(0,0)
root.title("calculator")
text_var=StringVar()


#creating frame for entry

ent_frame=Frame(root,width=312,height=60,bg="white")
entry=Entry(ent_frame,width=312,bg="white",textvariable=text_var,fg="black",highlightbackground="aqua",cursor="hand1")
ent_frame.pack()

entry.bind("<Return>",lambda event: equals())
entry.bind("<Delete>",lambda event:clear())
entry.bind("<s>",lambda event:square_show())
entry.bind("<q>", lambda  event: sqr_root())
entry.bind("<i>",lambda event : percentage())
entry.bind("<p>", lambda event : power())

entry.pack(ipady=15)

#frame just below button 
btn_frame=Frame(root,width=312,height=272.5)
btn_clear=Button(btn_frame,width=16,height=3,text="c",bg="#757575",cursor="hand2",highlightbackground="purple",command=clear)
btn_bkspce=Button(btn_frame,width=wid,height=3,text="bksp",bg="#757575", cursor="hand2",highlightbackground="purple",command= backspace)

#buttons
btn_divide=Button(btn_frame,width=wid,height=3,text="/",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("/"))
btn_1=Button(btn_frame,width=wid,height=3,text="1",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("1"))
btn_2=Button(btn_frame,width=wid,height=3,text="2",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("2"))
btn_3=Button(btn_frame,width=wid,height=3,text="3",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("3"))


btn_4=Button(btn_frame,width=wid,height=3,text="4",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("4"))
btn_5=Button(btn_frame,width=wid,height=3,text="5",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("5"))
btn_6=Button(btn_frame,width=wid,height=3,text="6",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("6"))

btn_7=Button(btn_frame,width=wid,height=3,text="7",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("7"))
btn_8=Button(btn_frame,width=wid,height=3,text="8",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("8"))
btn_9=Button(btn_frame,width=wid,height=3,text="9",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("9"))


btn_mult=Button(btn_frame,width=wid,height=3,text="*",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("*"))
btn_add=Button(btn_frame,width=wid,height=3,text="+",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("+"))
btn_subs=Button(btn_frame,width=wid,height=3,text="-",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("-"))


btn_0=Button(btn_frame,width=16,height=3,text="0",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("0"))
btn_dot=Button(btn_frame,width=wid,height=3,text=".",bg="#757575",cursor="hand2",highlightbackground="purple",command=lambda : action("."))
btn_eqlas=Button(btn_frame,width=wid,height=3,text="=",bg="#757575", cursor="hand2",highlightbackground="purple",command=equals)

btn_sqrt=Button(btn_frame,width=wid,height=3,text="sqrt(ctrl/q)",bg="#757575",cursor="hand2",highlightbackground="purple",command=sqr_root)
btn_square=Button(btn_frame,width=wid,height=3,text="sqr(ctrl/s)",bg="#757575",cursor="hand2",highlightbackground="purple",command=square_show)
btn_power=Button(btn_frame,width=wid,height=3,text="pow(ctrl/P)",bg="#757575",cursor="hand2",highlightbackground="purple",command=power)
btn_per=Button(btn_frame,width=wid,height=3,text="%(ctrl/i)",bg="#757575",cursor="hand2",highlightbackground="purple",command=percentage)




#packing it with grid method

btn_clear.grid(row=1,column=1,columnspan=2)
btn_divide.grid(row=1,column=4)
btn_bkspce.grid(row=1,column=3)


btn_7.grid(row=2,column=1)
btn_8.grid(row=2,column=2)
btn_9.grid(row=2,column=3)
btn_mult.grid(row=2,column=4)

btn_4.grid(row=3,column=1)
btn_5.grid(row=3,column=2)
btn_6.grid(row=3,column=3)
btn_subs.grid(row=3,column=4)

btn_1.grid(row=4,column=1)
btn_2.grid(row=4,column=2)
btn_3.grid(row=4,column=3)
btn_add.grid(row=4,column=4)


btn_eqlas.grid(row=5,column=4)
btn_0.grid(row=5,column=1 ,columnspan=2)
btn_dot.grid(row=5,column=3)

btn_square.grid(row=6,column=1)
btn_sqrt.grid(row=6,column=2)
btn_power.grid(row=6,column=4)
btn_per.grid(row=6,column=3)
btn_frame.pack(ipady=0)

root.mainloop()



