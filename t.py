from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")
def top():
    top =Toplevel()
    top.geometry("180x100" )
    top.title("toplevel")
    l2 = Label(top,text = "this is the top level window")
    l2.pack()
    top.mainloop()
l = Label(root,text = "this is the root window")
btn = Button(root,text = "click here to open another window",command = top)
l.pack()
btn.pack()
root.mainloop()