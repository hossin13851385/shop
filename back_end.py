import sqlite3

class Data:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS shop(name text , gheimat integer , forosh integer , number integer)")
        self.con.commit()

    def insert(self, name, price_gh, price_f, numbers):
        self.cur.execute("INSERT INTO shop VALUES (?,?,?,?)", (name, price_gh, price_f, numbers))
        self.con.commit()

    def search(self , name):
        self.cur.execute("""SELECT * FROM shop WHERE name LIKE ? or gheimat LIKE ? or forosh LIKE ? or number LIKE ? """, ( name+'%' , name+'%' , name+'%' , name+'%'))
        rows = self.cur.fetchall()
        return rows
    def delet(self ,name):
        self.cur.execute("DELETE FROM shop WHERE name=?", (name,))
        self.con.commit()
    def update(self ,rowid , name , price_gh , price_f , numbers):
        self.cur.execute("UPDATE shop SET name=? , gheimat=? , forosh=? , number=? WHERE rowid=? ",(name , price_gh , price_f , numbers , rowid))
        self.con.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM shop")
        rows = self.cur.fetchall()
        return rows

