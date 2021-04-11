import sqlite3


def Create():
    conn=sqlite3.connect("data.db")
    curs=conn.cursor()
    curs.execute("CREATE TABLE IF NOT EXISTS Product(Name TEXT, Ssn INTEGER)")
    conn.commit()
    conn.close()


def Insert(Name, Ssn):
    conn=sqlite3.connect("data.db")
    curs=conn.cursor()
    curs.execute("INSERT INTO Product VALUES(?,?)",(Name, Ssn))
    conn.commit()
    conn.close()

def View():
    conn=sqlite3.connect("data.db")
    curs=conn.cursor()
    curs.execute("SELECT * FROM Product")
    rows=curs.fetchall()
    print(rows)
    conn.commit()
    conn.close()

def Delete(Name):
        conn=sqlite3.connect("data.db")
        curs=conn.cursor()
        curs.execute("DELETE FROM Product WHERE Name=?", (Name,))
        conn.commit()
        conn.close()

def Update(Name, Ssn):
        conn=sqlite3.connect("data.db")
        curs=conn.cursor()
        curs.execute("UPDATE Product SET Ssn=? WHERE Name=?", (Name,Ssn))
        conn.commit()
        conn.close()


n=int(input("Enter choice: 1 Create, 2 Insert, 4 Delete, 5 Update, 6 View "))

if n==1: Create()
elif n==2: Insert('GreenTea', 12)
elif n==4: Delete('Coffee')
elif n==5: Update(15,'Tea')
else: View()
