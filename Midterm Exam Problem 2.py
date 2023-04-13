from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="Enter Given Name:")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text="Enter Middle Name:")
        self.lbl2.place(x=100, y=80)
        self.lbl3 = Label(win, text="Enter Last Name:")
        self.lbl3.place(x=100, y=110)
        self.lbl4 = Label(win, text="My Full Name is:")
        self.lbl4.place(x=100, y=150)
        self.lbl5 = Label(win, text= "My Full Name")
        self.lbl5.place(x=200, y=20)


        self.txt1 = Entry(win, bd=2)
        self.txt1.place(x=300, y=50)
        self.txt2 = Entry(win, bd=2)
        self.txt2.place(x=300, y=80)
        self.txt3 = Entry(win, bd=2)
        self.txt3.place(x=300, y=110)

        self.btn = Button(win, text="Show Full Name")
        self.btn.place(x=200, y=180)
        self.btn.bind('<Button-1>', self.show_full_name)

        self.full_name = Entry(win, bd=2, width=30)
        self.full_name.place(x=300, y=150)

    def show_full_name(self, event):
        full_name = self.txt1.get() + " " + self.txt2.get() + " " + self.txt3.get()
        self.full_name.delete(0, 'end')
        self.full_name.insert(0, full_name)

window = Tk()
mywin = MyWindow(window)
window.geometry("500x325+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()