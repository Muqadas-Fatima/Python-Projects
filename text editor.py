# Write your code here :-)
from tkinter import*
from  tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
obj=Tk()
obj.geometry("540x600")
obj.title(" Untitled - Notepad")
# text area

textarea=Text(obj,font=("Lucida",12))
textarea.pack(fill="both",expand=True)
s=Scrollbar(textarea)
s.pack(side="right",fill="y")
s.config(command=textarea.yview)
textarea.config(yscrollcommand=s.set)

file=None


def newfile():
    global file
    file=None
    obj.title("Untitled - File")
    textarea.delete(1.0,END)
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        obj.title(os.path.basename(file)+"- Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()
def save():
    global file
    if file is None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            obj.title(os.path.basename(file)+"- Notepad")

    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

def exit():
    obj.destroy()
def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")
def help_():
    showinfo("Notepad","Notepad by Muqadas")

# menuubar
m=Menu(obj)
filemenu=Menu(m,tearoff=0)
# file menu
filemenu.add_command(label="New",command=newfile)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(labe="Save",command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=exit)
m.add_cascade(label="File",menu=filemenu)

# edit menu
edit=Menu(m,tearoff=0)
edit.add_command(label="Cut",command=cut)
edit.add_command(label="Copy",command=copy)
edit.add_command(label="Paste",command=paste)
m.add_cascade(label="Edit",menu=edit)


# format menu
help=Menu(m,tearoff=0)
help.add_command(label="About Notepad",command=help_)
m.add_cascade(label="Help",menu=help)


obj.config(menu=m)
obj.mainloop()
