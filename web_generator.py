from tkinter import *
import webbrowser
import os

#setting the window size
win= Tk()
win.geometry('225x100')


# create a html file and adding its syntax 
def webPage():
    f = open('test1.html','x')
    #gets data from the "text" variable that the user enters
    htmlFormat= "<html><body><p>{}</p></body></html>".format(text.get())
    f.write(htmlFormat)
    webbrowser.open_new_tab('test1.html') # open in web browser on a new tab 


# button will call the webPage function and setting its location
btn = Button(win , text='Run', command=webPage)
btn.grid(row=0,column=0,padx=(10),pady=(10))
    
#Entry widget will let the user enter any data
text = Entry(win)
text.grid(row=0,column=1, columnspan=2, padx=(10), pady=(10))






