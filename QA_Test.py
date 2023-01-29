from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#set site's localhost IP Address and port, subdue to changes
global siteIPAddress, studentDataFileName, studentName, studentID
siteIPAddress, studentDataFileName = "127.0.0.1:522", "student-data.csv"

print(selenium.__version__)

#get student info from student data file:
def getStudentInfo(studentData):
    students = []
    global studentName, studentID
    with open(studentData, "r") as f:
        reader = csv.reader(f)
        for student in reader:
            students.append(student)
        # remove the headers from data
        students.pop(0)
        return students

#test if clicking the "Upload Data" button on the nav bar opens the correct oage
def test_goToUploadDataPage():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_button = driver.find_element(by=By.ID, value="upload-data-button")
    
    #Upload Data button is clicked
    upload_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "Upload Data"

    driver.quit()

#test if student data is uploaded successfully
def test_uploadStudentData():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_button = driver.find_element(by=By.ID, value="upload-data-button")
    
    #Upload Data button is clicked
    upload_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "Upload Data"

    driver.implicitly_wait(0.5)

    #find the upload file button and click it
    upload_student_data_button = driver.find_element(by=By.ID, value="upload-student-data-file")
    
    #Upload Student Data button is clicked
    upload_student_data_button.send_keys(studentDataFileName)

    studentData = getStudentInfo(studentDataFileName)

    #check if the right file is uploaded
    file_upload_message = driver.find_element(by=By.ID, value="upload-student-data-file-message").text
    assert file_upload_message + "File Uploaded:" + studentDataFileName

    driver.implicitly_wait(2)

    #find the button to enter Upload Data page, subdue to naming changes
    view_students_button = driver.find_element(by=By.ID, value="view-students-button")
    
    #Upload Data button is clicked
    view_students_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title2 = driver.title
    assert target_title2 == "View Students"

    driver.implicitly_wait(0.5)

    student_table = driver.findElement(By.id("View"));
    #get the size of the list of the rows
    totalRows = student_table.findElements(By.tagName("tr"))

    dataFound = False
    found = [False] * studentDataFileName.count()
    #find the student data, if found, set dataFound to true
    for s in studentData:
        for row in totalRows:
            student_name = row.findElements(By.id("student-name"))
            student_id = row.findElements(By.id("student-id"))
            #this should be the expected result
            if (student_name == s[1]) and (student_id == s[0]):
                index = studentData.index(s)
                found[index] = True

    for f in found:
        if f == False:
            dataFound == False
            break;
        else:
            dataFound = True
    
    if dataFound == False:
        print("Error! Student Data was not uploaded successfully!")

    driver.quit()

#test if student data file is wrong, an error message would show and the data should not be imported inside the database or be displayed
def test_uploadStudentData_Invalid():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_button = driver.find_element(by=By.ID, value="upload-data-button")
    
    #Upload Data button is clicked
    upload_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "Upload Data"

    driver.implicitly_wait(0.5)

    #find the upload file button and click it
    upload_student_data_button = driver.find_element(by=By.ID, value="upload-student-data-file")
    
    #Upload Student Data button is clicked
    upload_student_data_button.send_keys("invalid-student-data.xml")

    #check if the right file is uploaded
    file_upload_message = driver.find_element(by=By.ID, value="upload-student-data-error-message").text
    assert file_upload_message + "Error uploading student data"

    driver.implicitly_wait(2)

    #find the button to enter Upload Data page, subdue to naming changes
    view_students_button = driver.find_element(by=By.ID, value="view-students-button")
    
    #Upload Data button is clicked
    view_students_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title2 = driver.title
    assert target_title2 == "View Students"

    driver.implicitly_wait(0.5)

    student_table = driver.findElement(By.id("View"));
    #get the size of the list of the rows
    totalRows = student_table.findElements(By.tagName("tr"))

    studentData = getStudentInfo(studentDataFileName)

    dataFound = False
    found = [False] * studentDataFileName.count()
    #find the student data, if found, set dataFound to true
    for s in studentData:
        for row in totalRows:
            student_name = row.findElements(By.id("student-name"))
            student_id = row.findElements(By.id("student-id"))
            #this should be the expected result
            if (student_name == s[1]) and (student_id == s[0]):
                index = studentData.index(s)
                found[index] = True

    for f in found:
        if f == False:
            dataFound == False
            break;
        else:
            dataFound = True
    
    if dataFound == False:
        print("Error! Student Data was not uploaded successfully!")

    driver.quit()
