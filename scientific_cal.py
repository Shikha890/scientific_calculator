
# coding: utf-8

# In[22]:


from tkinter import *
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific calculator")
root.configure(background="powder blue")
root.resizable(width=False, height=False)
root.geometry("480x568+0+0")

cal = Frame(root)
cal.grid()

class calc():
    def __init__(self):
        self.total = 0
        self.now = ""
        self.input = True
        self.check = False
        self.op = ""
        self.result = False
        
    def number1(self, num):
        self.result = False
        firstnum = txtd.get()
        secondnum = str(num)
        if self.input:
            self.now = secondnum
            self.input = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.now = firstnum + secondnum
        self.display(self.now)
 # ------------------------EQUAL-----------------------------------
    def equal(self):
        self.result = True
        self.now = float(self.now)
        if self.check:
            self.valid()
        else:
            self.total = float(txtd.get())
# ------------------DISPLAY-----------------------------------
    def display(self, value):
        txtd.delete(0, END)
        txtd.insert(0, value)
 # -----------------------FUNCTION FOR SIMPLE CALCULATOR-----------------
    def valid(self):
        if self.op == "add":
            self.total += self.now
        if self.op == "minus":
            self.total -= self.now
        if self.op == "multi":
            self.total *= self.now
        if self.op == "div":
            self.total /= self.now
        if self.op == "mod":
            self.total %= self.now
        self.input = True
        self.display(self.total)
        
        
    def operation(self, op):
        self.now = float(self.now)
        if self.check:
            self.valid()
        elif not self.result:
            self.total = self.now
            self.input = True
        self.check = True
        self.op = op
        self.result = False
 # -------------------------------CLEAR---------------------------
    def clear(self):
        self.result = False
        self.now = 0
        self.display(0)
        self.input = True
 # ---------------------------all clear---------------------------
    def allclear(self):
        self.display(0)
        self.total = 0
        self.now = ""
        self.input = True
        self.check = False
        self.op = ""
        self.result = False
 # ---------------------------Function for pi --------------------------
    def pi(self):
        self.result = False
        self.now = math.pi
        self.display(self.now)
 # --------------Function for tan--------------------
    def tau(self):
        self.now = math.tau
        self.display(self.now)
 # -----------------Function for e----------------------
    def e(self):
        self.now = math.e
        self.display(self.now)
 # -----------------------Function for plus and minus---------------------
    def mathspm(self):
        self.now = -(float(txtd.get()))
        self.display(self.now)
 # ----------------function for square root------------------------
    def sqrt(self):
        self.now = math.sqrt(float(txtd.get()))
        self.display(self.now)
 # ------------------------function for sin----------------------
    def sin(self):
        self.result = False
        self.now = math.sin(math.radians(float(txtd.get())))
        self.display(self.now)
 # ------------------------function for cos----------------------
    def cos(self):
        self.now = math.cos(math.radians(float(txtd.get())))
        self.display(self.now)
 # ------------------------function for tan----------------------
    def tan(self):
        self.now = math.tan(math.radians(float(txtd.get())))
        self.display(self.now)
 # ------------------------function for sinh----------------------
    def sinh(self):
        self.now = math.sinh(math.radians(float(txtd.get())))
        self.display(self.now) # ------------------------function for cosh----------------------
    def cosh(self):
        self.now = math.cosh(math.radians(float(txtd.get())))
        self.display(self.now)
 # ------------------------function for tanh----------------------
    def tanh(self):
        self.now = math.tanh(math.radians(float(txtd.get())))
        self.display(self.now)
 # ------------------------function for exp----------------------
    def exp(self):
        self.now = math.exp(float(txtd.get()))
        self.display(self.now)
 # ------------------------function for sin----------------------
    def log(self):
        self.result = False
        self.now = math.log(float(txtd.get()))
        self.display(self.now)
 # ------------------------function for log2---------------------- 
    def log2(self):
        self.now = math.log2(float(txtd.get()))
        self.display(self.now)
 # ------------------------function for asinh----------------------
    def asinh(self):
        self.now = math.asinh(float(txtd.get()))
        self.display(self.now)
 # ------------------------function for acosh----------------------
    def acosh(self):
        self.now = math.acosh(float(txtd.get()))
        self.display(self.now)
        
added_value = calc()


txtd = Entry(cal, font=('arial', 20, 'bold'), bg="green", bd=30, width=28, justify=RIGHT)
txtd.grid(row=0, column=0, columnspan=4, pady=1)
txtd.insert(0, "0")
# ------------------For 1-9 numpad--------------------
number = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(cal, width=6, height=2, font=('arial', 20, 'bold'), bd=4, text=number[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x = number[i]: added_value.number1(x)
        i += 1
# -------------------------------------------Simple Button------------------
btnclear = Button(cal, text="c", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg="powder blue", command=added_value.clear).grid(row=1, column=0, pady=1)
btnallclear = Button(cal, text="ce", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg="powder blue", command=added_value.allclear).grid(row=1, column=1,pady=1)
btnsqrt = Button(cal, text="√", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powder blue", command=added_value.sqrt).grid(row=1, column=2, pady=1)
btnplus = Button(cal, text="+", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                 bg="powder blue", command=lambda: added_value.operation("add")).grid(row=1,column=3, pady=1)
btnminus = Button(cal, text="-", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg="powder blue", command=lambda:
                  added_value.operation("minus")).grid(row=2, column=3, pady=1)
btnmulti = Button(cal, text="*", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg="powder blue", command=lambda:
                  added_value.operation("multi")).grid(row=3, column=3, pady=1)
btndiv = Button(cal, text="/", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=lambda: added_value.operation("div")).grid(row=4,column=3, pady=1)
btnzero = Button(cal, text="0", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue", command=lambda: added_value.number1(0)).grid(row=5,column=0, pady=1)
btndot = Button(cal, text=".", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue", command=lambda: added_value.number1(".")).grid(row=5,column=1, pady=1)
btnmp = Button(cal, text="±", width=6, height=2, font=('arial', 20, 'bold'), bd=4,bg="powder blue", command=added_value.mathspm).grid(row=5, column=2, 
pady=1)
btnequal = Button(cal, text="=", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.equal).grid(row=5, column=3, pady=1)
# --------------------------------------------Scientific-----------------
btnpi = Button(cal, text="π", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
               bg="powder blue", command=added_value.pi).grid(row=1, column=4, pady=1)
btnsin = Button(cal, text="sin", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="powder blue", command=added_value.sin).grid(row=1, column=5, pady=1)
btncos = Button(cal, text="cos", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                bg="powder blue", command=added_value.cos).grid(row=1, column=6, pady=1)
btntan = Button(cal, text="tan", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.tan).grid(row=1, column=7, pady=1)
btntau = Button(cal, text="2π", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.tau).grid(row=2, column=4, pady=1)
btnsinh = Button(cal, text="sinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4, bg="powder blue", command=added_value.sinh).grid(row=2, column=5, pady=1)
btncosh = Button(cal, text="cosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.cosh).grid(row=2, column=6, pady=1)
btntanh = Button(cal, text="tanh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.tanh).grid(row=2, column=7, pady=1)
btnlog = Button(cal, text="log", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.log).grid(row=3, column=4, pady=1)
btnexp = Button(cal, text="Exp", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.exp).grid(row=3, column=5, pady=1)
btnmod = Button(cal, text="Mod", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=lambda: added_value.operation("mod")).grid(row=3, 
column=6, pady=1)
btne = Button(cal, text="e", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.e).grid(row=3, column=7, pady=1)
btnlog2 = Button(cal, text="log2", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.log2).grid(row=4, column=4, pady=1)
btndeg = Button(cal, text="deg", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue").grid(row=4, column=5, pady=1)
btnacosh = Button(cal, text="acosh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.acosh).grid(row=4, column=6, pady=1)
btnasinh = Button(cal, text="asinh", width=6, height=2, font=('arial', 20, 'bold'), bd=4,
 bg="powder blue", command=added_value.asinh).grid(row=4, column=7, pady=1)
lbl = Label(cal, text="Scientific Calculator", font=('arial', 30, 'bold'),
 justify=CENTER).grid(row=0, column=5, columnspan=4)
# -----------------------------menu------------#
def exit():
    exit = tkinter.messagebox.askyesno("Scientific calculaiotr", "confirm if you want to exit")
    if exit > 0:
        root.destroy()
        return
def simple():
    root.resizable(width=False, height=False)
    root.geometry("480x500+0+0")
def scientific():
    root.resizable(width=False, height=False)
    root.geometry("980x568+0+0")
    
menu = Menu(cal, font=('arial', 20, 'bold'))
filemenu = Menu(menu, font=('arial', 20, 'bold'))
menu.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="simple", command=simple)
filemenu.add_command(label="scientific", command=scientific)
filemenu.add_command(label="exit", command=exit)
root.config(menu=menu)
root.mainloop()

