from tkinter import *

root=Tk()
c1=Canvas(root,width=200,height=100)
c1.pack()
f1=Frame(c1)
f1.pack()
border=c1.create_rectangle(25,25,120,60,outline='grey',fill='red')
root.mainloop()
