import mysql.connector
conn = mysql.connector.connect(user='root', password='',
                              host='localhost',database='devops')

cursor = conn.cursor()
def create_table():
    cursor.execute("CREATE TABLE TEST (Name VARCHAR(50), Number VARCHAR(50))")
    cursor.execute("SELECT IF (EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'test'),'exist', 'nonexist')")
    results = cursor.fetchall()
    return results[0]