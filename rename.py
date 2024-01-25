import os
from tkinter import *


def rename(*args, new_name='', digits=1, ext=".txt"):
    n = 1
    if digits == 1:
        for arg in args:
            os.system(f'move {arg} {new_name}{str(n)}{ext}')
            n += 1
    elif digits == 2:
        for arg in args:
            if n < 10:
                os.system(f'move {arg} {new_name}0{str(n)}{ext}')
                n += 1
            else:
                os.system(f'move {arg} {new_name}{str(n)}{ext}')
                n += 1
    elif digits == 3:
        for arg in args:
            if n < 10:
                os.system(f'move {arg} {new_name}00{str(n)}{ext}')
                n += 1
            elif 10 <= n < 100:
                os.system(f'move {arg} {new_name}0{str(n)}{ext}')
                n += 1
            else:
                os.system(f'move {arg} {new_name}{str(n)}{ext}')
                n += 1


root = Tk()
root.title("Rename")

label1 = Label(root, text="New name: ")
label2 = Label(root, text="Extension: ")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1 = Entry(root, width=40)
entry2 = Entry(root, width=40)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)


def start():
    new_name = entry1.get()
    digits = 1
    ext = entry2.get()
    files = os.listdir()
    files.remove('rename.py')
    if 10 <= len(files) < 100:
        digits = 2
    elif len(files) >= 100:
        digits = 3

    if new_name and ext:
        rename(*files, new_name=new_name, digits=digits, ext=ext)
    elif not new_name and ext:
        rename(*files, digits=digits, ext=ext)
    elif new_name and not ext:
        rename(*files, new_name=new_name, digits=digits)
    elif not new_name and not ext:
        rename(*files, digits=digits)


button = Button(root, text="Start", command=start)
button.grid(row=2, column=1)

root.mainloop()
