from flask import Flask, render_template, request
import os
import Email
import mysql.connector

emailDirPath = ""
resumeDirPath = ""
conn = mysql.connector.connect(user='root', password='root',
                              host='localhost',database='devops')

cursor = conn.cursor()
app = Flask(__name__)

@app.route("/Main")
def home():
    return render_template("home.html")

@app.route("/Upload_Data", methods=['POST', 'GET'])
def upload_data():
    if request.method == 'POST':
        studentData = request.files['student-data-upload']
        companyData = request.files['company-data-upload']
    return render_template("upload_data.html")

@app.route("/Match_Student")
def match_student():
    cursor.execute("SELECT * FROM student")
    result = cursor.fetchall()
    cursor.execute("SELECT * FROM company")
    results = cursor.fetchall()
    return render_template("match_student.html", student_data = result, company_data = results)

@app.route("/Prepare_Email")
def prepare_email():
    return render_template("prepare_email.html")

@app.route("/Settings", methods=['POST', 'GET'])
def settings():
    global emailDirPath
    global resumeDirPath
    if request.method == 'POST':
        if 'submit-email-dir-btn' in request.form:
            emailDirPath = request.form.get("input-email-dir")
            #if check_path_exists(emailDirPath):
                # do smth
        elif 'submit-resume-dir-btn' in request.form:
            resumeDirPath = request.form.get("input-resume-dir")
            #if check_path_exists(resumeDirPath):
                # do smth

    return render_template("settings.html", emailPath = emailDirPath, resumePath = resumeDirPath)

# function that checks if directory exists and returns bool 
def check_path_exists(directory):
    check = os.path.isdir(directory)
    return check

if __name__ == '__main__':
    #host is to set the localhost IP Address, port is to set the port
    app.run(host = '127.0.0.1', port ='5221', debug = True)
