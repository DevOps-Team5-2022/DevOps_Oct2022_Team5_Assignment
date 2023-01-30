import mysql.connector
conn = mysql.connector.connect(user='root', password='',
                              host='localhost',database='devops')

cursor = conn.cursor()
def create_table():
    cursor.execute("CREATE TABLE TEST (Name VARCHAR(50), Number VARCHAR(50))")
    cursor.execute("SELECT IF (EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'test'),'exist', 'nonexist')")
    results = cursor.fetchall()
    return results[0]

def insert_record():
    cursor.execute("INSERT INTO TEST (Name, Number) VALUES ('devops','123456789')")
    conn.commit()
    cursor.execute("SELECT * FROM TEST")
    results = cursor.fetchall()
    if results != []:
        return "inserted"
    else:
        return "not inserted"

def update_record():
    cursor.execute("UPDATE TEST SET Name = 'notdevops' WHERE Number = '123456789'")
    conn.commit()
    cursor.execute("SELECT * FROM TEST WHERE Number = '123456789'")
    results = cursor.fetchall()
    if results != []:
        if results[0][0] == 'notdevops':
            return "true"
        else:
            return "false"
    else:
        return "false" 

def delete_record():
    cursor.execute("DELETE FROM TEST WHERE Number = '123456789'")
    conn.commit()
    cursor.execute("SELECT * FROM TEST WHERE Number = '123456789'")
    results = cursor.fetchall()
    if results != []:
        return "true"
    else:
        return "false" 

def delete_table():
    cursor.execute("DROP TABLE TEST")
    cursor.execute("SELECT IF (EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'test'),'exist', 'nonexist')")
    results = cursor.fetchall()
    return results[0]