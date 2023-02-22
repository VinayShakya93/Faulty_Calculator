from tkinter import *
def click(event):
    global scvalue
    text= event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value= int(scvalue.get())
        else:
            value= eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root=Tk()
root.geometry('455x650')
root.title('Calculator')
root.wm_iconbitmap("Calculator.ico")
root.configure(background="grey")

scvalue= StringVar()
scvalue.set("")
screen= Entry(root, textvar=scvalue, bg='orange',font="lucida 45 bold")
screen.pack(pady=20, padx=10, ipadx=20,ipady=5)

f= Frame(root )
b= Button(f, text='1',pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='2', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='3', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

f.pack()

f= Frame(root )
b= Button(f, text='4', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='5', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='6', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root )
b= Button(f, text='7', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='8', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='9', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()


f= Frame(root )
b= Button(f, text='0', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='00', pady=5, padx=35,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='.', pady=5, padx=40,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root )
b= Button(f, text='+', pady=2, padx=9,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='-', pady=2, padx=17,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='*', pady=2, padx=17,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='/', pady=2, padx=17,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='%', pady=2, padx=10,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f= Frame(root )
b= Button(f, text='C', pady=5, padx=33,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='=', pady=5, padx=30,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)

b= Button(f, text='BACK', pady=5, padx=15,font='lucida 25 bold')
b.pack(side=LEFT, padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()



root.mainloop()