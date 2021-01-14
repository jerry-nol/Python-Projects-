import sqlite3 #importing sqlite3 module

conn = sqlite3.connect('db_assignment.db')

fileList = ('information.docx','Hello.txt', 'myImage.png', 'myMovie.mpg','World.txt', 'data.pdf','myPhoto.jpg') #file documents names 

with conn:
    cur = conn.cursor()
    #Naming the table and attributes
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT) \
        ")
    conn.commit() #commits all commands 
conn.close() #closes with statement






conn = sqlite3.connect('db_assignment.db')

with conn:
    cur = conn.cursor()
    for i in fileList: # for loop that iterates through the fileList
        if i.endswith('.txt'): #select files that end with .txt
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?) ",\
            (i,))
            print(i)
    conn.commit()
conn.close()
