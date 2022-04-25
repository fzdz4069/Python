import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abcde12345",
    database="bk")

cur = mydb.cursor()

insert = "insert into arch values (%s, %s, %s, %s, %s, %s, %s)"
folder_0 = ("00_00_00", "ex", "video", 0.0, "1.1", "2.3", 0)
folder_1 = ("00_00_01", "ex", "foto", "1.0", "0.1", "0.8", 0)
folder_2 = ("00_00_02", "ex", "video", "1.9", "2.1", 0.0, 0)

cur.execute(insert, folder_0)
cur.execute(insert, folder_1)
cur.execute(insert, folder_2)

mydb.commit()

cur.close()
mydb.close()
