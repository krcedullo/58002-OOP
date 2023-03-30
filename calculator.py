from tkinter import *

class MyWindow:
    def __init__(self, win):
        # widgets start from here
        self.lbl1 = Label(win, text="Enter a number: ")
        self.lbl1.grid(row=0, column=0, padx=5, pady=5)

        self.txt1 = Entry(win, bd=1)
        self.txt1.grid(row=0, column=1, padx=5, pady=5)

        self.lbl2 = Label(win, text="Enter a second number: ")
        self.lbl2.grid(row=1, column=0, padx=5, pady=5)

        self.txt2 = Entry(win, bd=1)
        self.txt2.grid(row=1, column=1, padx=5, pady=5)

        self.lbl3 = Label(win, text="Result: ")
        self.lbl3.grid(row=2, column=0, padx=5, pady=5)

        self.txt3 = Entry(win, bd=3)
        self.txt3.grid(row=2, column=1, padx=5, pady=5)

        self.btnadd = Button(win, text="Add", width=10, command=self.add)
        self.btnadd.grid(row=3, column=0, padx=5, pady=5)

        self.btnsub = Button(win, text="Subtract", width=10, command=self.sub)
        self.btnsub.grid(row=4, column=0, padx=5, pady=5)

        self.btnmul = Button(win, text="Multiply", width=10, command=self.mul)
        self.btnmul.grid(row=5, column=0, padx=5, pady=5)

        self.btndiv = Button(win, text="Divide", width=10, command=self.div)
        self.btndiv.grid(row=6, column=0, padx=5, pady=5)

        self.btnclear = Button(win, text="Clear", width=10, command=self.clear)
        self.btnclear.grid(row=7, column=0, padx=5, pady=5)

    def add(self):
        self.txt3.delete(0, END)
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END, str(result))

    def sub(self):
        self.txt3.delete(0, END)
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 - num2
        self.txt3.insert(END, str(result))

    def mul(self):
        self.txt3.delete(0, END)
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def div(self):
        self.txt3.delete(0, END)
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        if num2 == 0:
            self.txt3.insert(END, "Error: Division by zero")
        else:
            result = num1 / num2
            self.txt3.insert(END, str(result))

    def clear(self):
        self.txt1.delete(0, END)
        self.txt2.delete(0, END)
        self.txt3.delete(0, END)


window = Tk()
mywin = MyWindow(window)
window.geometry("300x300")
window.title("Simple Calculator")
window.mainloop()
