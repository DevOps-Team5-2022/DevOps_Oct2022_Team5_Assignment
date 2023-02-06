import pandas as pd
from independentsoft.msg import Message
from independentsoft.msg import Attachment
from independentsoft.msg import Recipient
from independentsoft.msg import ObjectType
from independentsoft.msg import DisplayType
from independentsoft.msg import RecipientType
from independentsoft.msg import MessageFlag
from independentsoft.msg import StoreSupportMask
import os
from datetime import datetime

# function to try to upload data to database
def upload_data_func(file, tableName, engine):
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

# validation for file uploaded in upload_data page
def validate_upload_file(data, fileName, tableName, engine):
    extension = fileName.split(".")[1]
    # check file extension is one of the excel files
    if extension == "csv" or extension == "xlsx" or extension == "xls":
        dataDF = pd.read_excel(data)
        # if excel is empty
        if dataDF.empty:
            msg = 'error'
        else:
            msg = upload_data_func(dataDF, tableName, engine)
    else:
        msg = 'error'
    
    return msg

# convert date object to string
def date_to_str(startDate, endDate):
    startDay = startDate.day
    startMonth = startDate.month
    startYear = str(startDate.year)
    if startDay < 10:
        startDay = "0" + str(startDay)
    else:
        startDay = str(startDay)

    if startMonth < 10:
        startMonth = "0" + str(startMonth)
    else:
        startMonth = str(startMonth)
    

    endDay = endDate.day
    endMonth = endDate.month
    endYear = str(endDate.year)
    if endDay < 10:
        endDay = "0" + str(endDay)
    else:
        endDay = str(endDay)

    if endMonth < 10:
        endMonth = "0" + str(endMonth)
    else:
        endMonth = str(endMonth)
    
    finalStartDate = startDay + "/" + startMonth + "/" + startYear
    finalEndDate = endDay + "/" + endMonth + "/" + endYear

    return finalStartDate, finalEndDate

# initialize config table in database
def init_config_table(conn, cursor):
    cursor.execute("CREATE TABLE config (ID int, resume_path text, email_path text, internship_period_start date, internship_period_end date)")
    conn.commit()

    today = datetime.today().strftime("%Y/%m/%d")
    cursor.execute("INSERT INTO config (ID) VALUES (1)")
    conn.commit()
    cursor.execute("UPDATE config SET resume_path = (%s), email_path = (%s), internship_period_start = (%s), internship_period_end = (%s) WHERE ID = 1", (None, None, today, today))
    conn.commit()

# update config table with new inputted directory
def update_directory(columnName, directoryPath, cursor, conn):
    if columnName == "email":
        if os.path.isdir(directoryPath):
            cursor.execute("UPDATE config SET email_path = (%s) WHERE ID = (%s)", (directoryPath, 1))
            conn.commit()
            result = 'success'
        else:
            result = 'error'

    elif columnName == "resume":
        if os.path.isdir(directoryPath):
            cursor.execute("UPDATE config SET resume_path = (%s) WHERE ID = (%s)", (directoryPath, 1))
            conn.commit()
            result = 'success'
        else:
            result = 'error'       

    return result

# string email, string recipientName, string beforeDate, string afterDate
def create_email(email, recipientName, beforeDate, afterDate):
    message = Message()
    year =  beforeDate[-4:]

    # Create Recipient
    companyContact = Recipient()
    companyContact.address_type = "SMTP"
    companyContact.display_type = DisplayType.MAIL_USER
    companyContact.object_type = ObjectType.MAIL_USER
    companyContact.display_name = recipientName
    companyContact.email_address = email
    companyContact.recipient_type = RecipientType.TO

    #
    message.subject = "Internship Response to Internship Request"
    message.body = "Dear " + companyContact.display_name + ",\nKindly find attached our students resume for the " + year + \
                   " semester Internship in response to your job description which you have submitted to us." + \
                   "\nWe look forward to your favorable response and to working with your company for the upcoming internship period " + \
                   beforeDate + " to " + afterDate
    
    message.display_to = recipientName
    #message.display_cc = ""
    message.recipients.append(companyContact)
    message.message_flags.append(MessageFlag.UNSENT)
    #message.store_support_masks.append(StoreSupportMask.CREATE)

    return message

def save_email(message, filePath):
    try:
        message.save(os.path.join(filePath, message.recipients[0].display_name + " Internship Email.msg"))
    except:
        return "fail"
    else:
        return "success"
