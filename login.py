from tkinter import *


def actperformed(event):
    get_name=name_entry.get()
    get_pass=name_entry.get()
    if(get_name=='admin' and get_pass=='admin'):
        
        nw=Tk()
        nw['bg']='black'
        nw.geometry("1280x720")

        nwl1=Label(nw,text='login succesfull',fg='white',bg='black')
        nwl1.pack()

root = Tk()
root["bg"]="black"  


c3=Canvas(root,width=640,height=480,bg='black')
c3.pack()
c2=Canvas(c3,width=640,height=480,bg='black')
c2.pack()
c1=Canvas(c2,width=640,height=480,bg='black')
c1.pack()


#initialize
title=Label(c2,text='"WELCOME TO WEB CRAWLER"',anchor='n',fg='yellow',bg='black',width=30)
title.config(font=("Courier", 20))
name= Label(c1,text='Name',bg='black',fg='red')
password=Label(c1,text='Password',bg='black',fg='blue')
name_entry=Entry(c1,bg='grey')
pass_entry=Entry(c1,bg='grey',show='*')
button = Button(c1,bg='white',activebackground='green',fg='black',text='login',width=5,height=1,font=("Arial", 10))
border=c2.create_rectangle(20,20,620,460,fill='black',outline='white')


#packing
title.place(relx=0.5, rely=0.1,anchor='n')
name.grid(row =2,column=2,sticky=E,padx=1,pady=2)
password.grid(row=3,column=2,sticky=E,padx=2,pady=2)
name_entry.grid(row=2,column=3,padx=3,pady=2)
pass_entry.grid(row=3,column=3,padx=3,pady=2)
button.grid(row=4,column=3,sticky=W,padx=4,pady=5)
button.bind("<Button-1>",actperformed)
c1.place(relx=0.5, rely=0.5, anchor=CENTER)


#retriving

root.mainloop()
