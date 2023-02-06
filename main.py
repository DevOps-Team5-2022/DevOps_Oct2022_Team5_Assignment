from flask import Flask, render_template, request, flash
import os
from datetime import date
import functions
import mysql.connector
import pytest
import pandas as pd
from sqlalchemy import create_engine

conn = mysql.connector.connect(user='root', password='root',
                              host='localhost',database='devops', connect_timeout=1000)

# this is for uploading excel data into the sql db, mysql.connector doesnt work
engine = create_engine("mysql://{user}:{pw}@{host}/{db}"
				.format(host='localhost', db='devops', user='root', pw='root'))



cursor = conn.cursor()
app = Flask(__name__)

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
        if studentData.filename != "":
            msg = functions.validate_upload_file(studentData, studentData.filename, 'student', engine)
            if msg == 'success':
                sDataSuccess = True
            else:
                sDataSuccess = False    
            
        if companyData.filename != '':
            msg = functions.validate_upload_file(companyData, companyData.filename, 'company', engine)
            companyExtension = companyData.filename.split(".")[1]
            if msg == 'success':
                cDataSuccess = True
            else:
                cDataSuccess = False

        
    return render_template("upload_data.html", result = msg, success1 = sDataSuccess, success2 = cDataSuccess)

@app.route("/Match_Student")
def match_student():
    
    # get all data from student table
    cursor.execute("SHOW TABLES LIKE 'student'")
    checkExists = cursor.fetchall()
    # if student table exists
    if len(checkExists) > 0:
        cursor.execute("SELECT * FROM student")
        result = cursor.fetchall()

    # if student table doesn't exists
    else:
        result = None

    # get all data from company table
    cursor.execute("SHOW TABLES LIKE 'company'")
    checkExists = cursor.fetchall()
    # if company table exists
    if len(checkExists) > 0:
        cursor.execute("SELECT * FROM company")
        results = cursor.fetchall()

    # if company table doesn't exists
    else:  
        results = ()
    
    return render_template("match_student.html", student_data = result, company_data = results)

@app.route("/Prepare_Email")
def prepare_email():
    return render_template("prepare_email.html")

@app.route("/Settings", methods=['POST', 'GET'])
def settings():
    check = [False, False]
    valid = [False, False]
    
    # gets directory from Database
    cursor.execute("SHOW TABLES LIKE 'config'")
    checkExists = cursor.fetchall()

    # if table doesnt exist, create table and add demo record
    if len(checkExists) == 0:
        cursor.execute("CREATE TABLE config (ID int, resume_path text, email_path text, internship_period_start date, internship_period_end date)")
        conn.commit()

        today = date.today().strftime("%Y/%m/%d")
        cursor.execute("INSERT INTO config (ID) VALUES (1)")
        conn.commit()
        cursor.execute("UPDATE config SET resume_path = (%s), email_path = (%s), internship_period_start = (%s), internship_period_end = (%s) WHERE ID = 1", (None, None, today, today))
        conn.commit()
        
    cursor.execute("SELECT * FROM config")
    configTuple = cursor.fetchall()

    emailDirPath = configTuple[0][2]
    resumeDirPath = configTuple[0][1]

    startDate, endDate = functions.date_to_str(configTuple[0][3], configTuple[0][4])

    
    if request.method == 'POST':
        if 'submit-email-dir-btn' in request.form:
            emailDirPath = request.form.get("input-email-dir")
            if os.path.isdir(emailDirPath):
                valid[0] = True
                cursor.execute("UPDATE config SET email_path = (%s) WHERE ID = (%s)", (emailDirPath, 1))
                conn.commit()
            else:
                valid[0] = False

            check[0] = True
        elif 'submit-resume-dir-btn' in request.form:
            resumeDirPath = request.form.get("input-resume-dir")
            if os.path.isdir(resumeDirPath):
                valid[1] = True
                cursor.execute("UPDATE config SET resume_path = (%s) WHERE ID = (%s)", (resumeDirPath, 1))
                conn.commit()
            else:
                valid[1] = False
            check[1] = True

        elif 'submit-internship-period-btn' in request.form:
            startDate = request.form.get("inputted-start-date")
            endDate = request.form.get("inputted-end-date")

            cursor.execute("UPDATE config SET internship_period_start = (%s), internship_period_end = (%s) WHERE ID = 1", (startDate, endDate))
            conn.commit()

            startDate = startDate[8:] + "/" + startDate[5:7] + "/" + startDate[0:4]
            endDate = endDate[8:] + "/" + endDate[5:7] + "/" + endDate[0:4]
            
        
    return render_template("settings.html", emailPath = emailDirPath, resumePath = resumeDirPath, startDate = startDate, endDate = endDate, check = check, valid = valid)


if __name__ == '__main__':
    #host is to set the localhost IP Address, port is to set the port
    app.run(host = '127.0.0.1', port ='5221', debug = True)
