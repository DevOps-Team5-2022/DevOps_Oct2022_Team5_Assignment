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

#create_email("s10194152@connect.np.edu.sg", "Tan Jun Jie", "29/1/2023", "29/7/2023", "D:\\Documents")
#message = create_email("s10194152@connect.np.edu.sg", "Tan Jun Jie", "29/1/2023", "29/7/2023")
#results = save_email(message, "D:\\Documents")
#print(results)

