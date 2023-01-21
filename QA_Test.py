from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#set site's localhost IP Address and port, subdue to changes
global siteIPAddress, studentDataFileName, studentName, studentID
siteIPAddress, studentDataFileName = "127.0.0.1:522", "student-data.csv"
studentName, studentID = "Sean Lim Jie En", "S10201234"

#test if clicking the "Upload Data" button on the nav bar opens the correct oage
def test_goToUploadDataPage():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get(siteIPAddress)

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

    driver.get(siteIPAddress)

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
    #find the student data, if found, set dataFound to true
    for row in totalRows:
        student_name = row.findElements(By.id("student-name"))
        student_id = row.findElements(By.id("student-id"))
        if student_name == studentName && student_id == studentID:
            dataFound = True
            break;
    if dataFound == False:
        print("Error! Student Data was not uploaded successfully!")

    driver.quit()