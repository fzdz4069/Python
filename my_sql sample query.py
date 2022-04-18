import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="ffzzddzz44006699",
    database="bk")

cursor = mydb.cursor()

query = "select a.folder from arch as a " \
        "where a.media like '%video%';"

file = open("temp.txt", "w")

cursor.execute(query)
n = 0
for col in cursor:
    file.write("folder_" + str(n) + " = ('" + str(col) + "', )\n")
    n += 1

file.close()
cursor.close()
mydb.close()
