import sqlite3


def Create():
    conn=sqlite3.connect("Back.db")
    curs=conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS Cars(id INTEGER PRIMARY KEY, ModelName TEXT, Company TEXT, Year INTEGER, ChasisNo INTEGER)")
    conn.commit()
    conn.close()


def Insert(ModelName, Company, Year, ChasisNo):
    conn=sqlite3.connect("Back.db")
    curs=conn.cursor()
    curs.execute("INSERT INTO Cars VALUES(NULL,?,?,?,?)",(ModelName, Company, Year, ChasisNo))
    conn.commit()
    conn.close()

def View():
    conn=sqlite3.connect("Back.db")
    curs=conn.cursor()
    curs.execute("SELECT * FROM Cars")
    rows=curs.fetchall()
    return rows
    conn.commit()
    conn.close()

def Delete(id):
        conn=sqlite3.connect("Back.db")
        curs=conn.cursor()
        curs.execute("DELETE FROM Cars WHERE id=?", (id,))
        conn.commit()
        conn.close()

def Update(id, ModelName, Company, Year, ChasisNo):
        conn=sqlite3.connect("Back.db")
        curs=conn.cursor()
        curs.execute("UPDATE Cars SET ModelName=? OR Company=? OR Year=? OR ChasisNo=? WHERE id=?", (id, ModelName, Company, Year, ChasisNo))
        conn.commit()
        conn.close()

def Search(ModelName="", Company="", Year="", ChasisNo=""):
        conn=sqlite3.connect("Back.db")
        curs=conn.cursor()
        curs.execute("SELECT * FROM Cars WHERE ModelName=? OR Company=? OR Year=? OR ChasisNo=?", (ModelName, Company, Year, ChasisNo))
        rows=curs.fetchall()
        return rows
        conn.commit()
        conn.close()
