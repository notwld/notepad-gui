from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from base64 import b64encode,b64decode

win=Tk()
win.title('Not a pad')
win.geometry("720x690")
textarea=Text(win, font="lucida 15",bg='black',fg='green')
file=None
textarea.pack(expand=True, fill=BOTH)

menu=Menu(win)


def new_file():
    global file
    win.title('Congratulations u have made a new file!')
    file=None
    textarea.delete(1.0 ,'end')

def file_open():
    global file
    file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
    if file == "":
        file=None
    else:
        f=open(file,'r')
        win.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, 'end')
        textarea.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file==None:
        file=asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            f=open(file,'r')
            f.write(textarea.get(1.0, 'end'))
            f.close()

            win.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f=open(file, "w")
        f.write(textarea.get(1.0,'end'))
        f.close()

file_menu=Menu(menu,tearoff=0)
file_menu.add_command(label='New File',command=new_file)
file_menu.add_command(label='Open File',command=file_open)
file_menu.add_command(label='Save File',command=save)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=win.destroy)
menu.add_cascade(label='File',menu=file_menu)

def encr():
    a=textarea.get(1.0,'end')
    s=''
    for i in a:
        s=s+str(i)
    en=b64encode(s.encode())
    textarea.delete(1.0,'end')
    textarea.insert(1.0,en)

def dencr():
    a=textarea.get(1.0,'end')
    s=''
    for i in a:
        s=s+str(i)
    en=b64decode(s.encode())
    textarea.delete(1.0,'end')
    textarea.insert(1.0,en)


edit_menu=Menu(menu,tearoff=0)
edit_menu.add_command(label='Cut',accelerator="Ctrl+x",command=lambda:textarea.focus_get().event_generate('<<Cut>>'))
edit_menu.add_command(label='Copy',accelerator="Ctrl+c",command=lambda:textarea.focus_get().event_generate('<<Copy>>'))
edit_menu.add_command(label='Paste',accelerator="Ctrl+v",command=lambda:textarea.focus_get().event_generate('<<Paste>>'))
edit_menu.add_command(label='Select all',accelerator="Ctrl+a",command=lambda:textarea.focus_get().event_generate('<<Select>>'))
edit_menu.add_command(label='Encrypt text',command=encr)
edit_menu.add_command(label='Decrypt text',command=dencr)
menu.add_cascade(label='Edit',menu=edit_menu)

def about():
    messagebox.showinfo('About','Ver 0.1.0\nMade by Levi')

About=Menu(menu,tearoff=0)
About.add_command(label='Credits',command=about)
menu.add_cascade(label='About',menu=About)

win.config(menu=menu)

def on_closing():
        if messagebox.askokcancel("Quit", "Make sure to save ur file.. Take care :)"):
            win.destroy()

win.protocol("WM_DELETE_WINDOW", on_closing)
win.mainloop()