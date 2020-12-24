import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()


class users:
    def Validate_user(email,password):
        if "@" not in email :
            return False
        if "." not in email:
            return False
        c.execute("SELECT * FROM stuffToPlot")
        data = c.fetchall()
        for row in data:
            if row[0]==email and password==row[1]:
                return True
            else:
                return False


##print(users.Validate_user("yassataiseer@gmail.com","yassa123"))

