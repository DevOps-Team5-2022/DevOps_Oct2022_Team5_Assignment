from flask import Flask, render_template, request, flash
import os
import Email
import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

emailDirPath = ""
resumeDirPath = ""
conn = mysql.connector.connect(user='root', password='root',
                              host='localhost',database='devops')

# this is for uploading excel data into the sql db, mysql.connector doesnt work
engine = create_engine("mysql://{user}:{pw}@{host}/{db}"
				.format(host='localhost', db='devops', user='root', pw='root'))



cursor = conn.cursor()
app = Flask(__name__)

# required for using flash()
app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/Main")
def home():
    return render_template("home.html")

@app.route("/Upload_Data", methods=['POST', 'GET'])
def upload_data():
    msg = ''
    sDataSuccess = False
    cDataSuccess = False
    if request.method == 'POST':
        studentData = request.files['student-data-upload']
        companyData = request.files['company-data-upload']
        print(studentData)
        if studentData.filename != '':
            studentDataDF = pd.read_excel(studentData)
            msg = upload_data_func(studentDataDF, 'student')
            if msg == 'success':
                sDataSuccess = True
            else:
                sDataSuccess = False
            
        if companyData.filename != '':
            companyDataDF = pd.read_excel(companyData)
            msg = upload_data_func(companyDataDF, 'company')
            if msg == 'success':
                cDataSuccess = True
            else:
                cDataSuccess = False

        
    return render_template("upload_data.html", result = msg, success1 = sDataSuccess, success2 = cDataSuccess)

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

# function to try to upload data to database
def upload_data_func(file, tableName):
    try:
        file.to_sql(tableName, engine, if_exists='append', index = False)
    except:
        # error with uploading
        return 'error'
        flash('Invalid Table Format', 'error')
    else:
        # success with uploading
        return 'success'
        flash('Upload Successful!')

if __name__ == '__main__':
    #host is to set the localhost IP Address, port is to set the port
    app.run(host = '127.0.0.1', port ='5221', debug = True)
