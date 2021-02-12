from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import shutil
import os
from datetime import datetime, timedelta

#main window title and min/max size
win = Tk()
win.title('Choose Directories')
win.minsize(700,500)
win.maxsize(700,500)


def search():
   address = fd.askdirectory()
   entry1.insert(0,address)

def search2():
   address = fd.askdirectory()
   entry2.insert(0,address)

def update():
    #user chooses the path they want
    src = entry1.get()+'\\'

    dest = entry2.get()+'\\'
    files = os.listdir(src)
    last__day_time = datetime.now() - timedelta(hours = 24)
    
    for i in files: #for loop for files in src
        mod_time = os.stat(src+i).st_mtime #the seconds in which files have been last modified
        Mod_time_hours= datetime.fromtimestamp(mod_time) #converting the seconds in to a date and time
        #If any files have been added/modified in the last 24 hours, move to destination folder
        if Mod_time_hours > last__day_time: 
             shutil.move(src+i, dest)

# this funtion when called will ask user to confirm exit
def close():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        win.destroy()
   

#Buttons and locations 
btn1 = Button(win,text='Browse', command=search)
btn1.grid(row=0, column=0, padx=(10,2), pady=(10,2))
btn2 = Button(win,text='Browse', command=search2)
btn2.grid(row=1, column=0, padx=(10,2), pady=(10,2))
btn3 = Button(win,text='Close', command=close,bg='white', fg='red').grid(row=2 ,column=3,padx=(10,2), pady=(10,2))
btn4 = Button(win,text='Check for files',command=update).grid(row=2,column=0,pady=(10),sticky=E+N)


#Entry box and location
entry1 = Entry(win)
entry1.grid(row=0,column=1,columnspan=3,padx=(10,2), pady=(10,2))
entry2 = Entry(win)
entry2.grid(row=1,column=1,columnspan=3,padx=(10,2), pady=(10,2))




win.mainloop()
