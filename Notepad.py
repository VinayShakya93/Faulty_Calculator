import os.path
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textarea.delete(1.0, END)

def openfile():
    global file
    file= askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textarea.delete(1.0,END)
        f=open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='untitled.txt',defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents","*.txt")] )
        if file=="":
            file=None
        else:
            # save as new file
            f=open(file,"w")
            f.write(textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + "-Notepad")
    else:
        # save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()

def quitapp():
    root.destroy()

def cut():
    textarea.event_generate(("<<Cut>>"))

def copy():
    textarea.event_generate(("<<Copy>>"))

def paste():
    textarea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Vinay")

if __name__ == '__main__':
    #basic tkinter setup
    root=Tk()
    root.title("untitled- Notepad")
    root.wm_iconbitmap("notepad-icon_34386.ico")
    root.geometry("555x455")

    # add text area
    textarea=Text(root, font="lucida 12")
    file=None
    textarea.pack(fill=BOTH, expand=True)
    # lets create menu bar
    menubar=Menu(root)

    #file menu start
    filemenu=Menu(menubar, tearoff=0)

    #to open new file
    filemenu.add_command(label="New", command= newfile)

    #to open already existing file
    filemenu.add_command(label="Open", command=openfile)

    # to save current file

    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    # to exit
    filemenu.add_command(label="Exit", command=quitapp)
    menubar.add_cascade(label="File", menu=filemenu)
    # end filemenu

    #start editbar
    Editmenu=Menu(menubar,tearoff=0)
    Editmenu.add_command(label="Cut",command=cut)
    Editmenu.add_command(label="Copy",command=copy)
    Editmenu.add_command(label="paste",command=paste)

    menubar.add_cascade(label="Edit", menu=Editmenu)
    # end editmenu
    # help menu start
    Helpmenu=Menu(menubar, tearoff=0)
    Helpmenu.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=Helpmenu)

    root.config(menu=menubar)
# adding scroll bar
    scroll=Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    Scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand= scroll.set)
    root.mainloop()