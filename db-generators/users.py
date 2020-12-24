import sqlite3
### Do not run the code as it will create a new user code was only meant to write into a database
conn = sqlite3.connect('users.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(email TEXT, password TEXT)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES('yassataiseer@gmail.com','yassa123'  )")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()