import sqlite3

conn = sqlite3.connect('db_assignment.db')

fileList = ('information.docx','Hello.txt', 'myImage.png', 'myMovie.mpg','World.txt', 'data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor() 
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name)
        ")
    conn.commit()
conn.close()






conn = sqlite3.connect('db_assignment.db')

with conn:
    cur = conn.cursor()
    for i in fileList:
        if file.endswith('.txt'):
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?) ",\
            (i,))
            print(i)
    conn.commit()
conn.close()
