import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="abcde12345",
    database="bk")

cur = mydb.cursor()

cur.execute("CREATE table arch ("
            "folder varchar(20) primary key,"
            "typ varchar(20),"
            "media varchar(20),"
            "GB_arch_3 decimal(3, 1),"
            "GB_arch_1 decimal(3, 1),"
            "GB_arch_2 decimal(3, 1),"
            "id int);")


