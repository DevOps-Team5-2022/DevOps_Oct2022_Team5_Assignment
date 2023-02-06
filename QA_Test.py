import csv

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#set site's localhost IP Address and port
global siteIPAddress, studentDataFileName, companyDataFileName #
siteIPAddress = "http://127.0.0.1:5221"
studentDataFileName = "studentData.csv"
companyDataFileName = "companyDataFile.csv"

print(selenium.__version__)

# Kevin's test cases
def test_goToMainPage():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"
    driver.quit()
    
def test_wrongFileType_uploadCompanyData():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

    driver.get(siteIPAddress + "/Upload_Data")

    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Upload Data Page"

    chooseFile = driver.find_element("xpath", "//*[@id='company-data-upload']")
    submitButton = driver.find_element("xpath",'//*[@id="upload-data-form"]/input[3]')

    driver.implicitly_wait(3)

    #chooseFile.send_keys("C:/Users/imsam/Downloads/GPA_sample_calculation_v1.xls")
    #chooseFile.send_keys("C:/Users/imsam/Downloads/companyDataFile.csv")
    chooseFile.send_keys("/home/runner/work/DevOps_Oct2022_Team5_Assignment/DevOps_Oct2022_Team5_Assignment/testFail.csv")
    submitButton.click()

    submitMsg = driver.find_element("xpath", "//*[@id='file-upload-error-txt']")

    assert submitMsg.text == "Upload Failed. Invalid Format"

    driver.quit()

# Samuel's Test cases
#get student info from student data file:
def getStudentInfo(studentData):
    students = []
    with open(studentData, "r") as f:
        reader = csv.reader(f)
        for student in reader:
            students.append(student)
        # remove the headers from data
        students.pop(0)
        return students
    

#get student info from student data file:
def getCompanyInfo(companyData):
    companies = []
    with open(companyData, "r") as f:
        reader = csv.reader(f)
        for company in reader:
            companies.append(company)
        # remove the headers from data
        companies.pop(0)
        return companies

#test if clicking the "Upload Data" button on the nav bar opens the correct oage
def test_goToUploadDataPage():
    options = Options()
    options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_data_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[1]/a')
    
    #Upload Data button is clicked
    upload_data_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Upload Data Page"

    driver.quit()

#test if clicking the "Prepare Email" button on the nav bar opens the correct oage
def test_goToPrepareEmailPage():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    prepare_email_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[3]/a')
    
    #Upload Data button is clicked
    prepare_email_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Prepare Email Page"

    driver.quit()


#test if clicking the "Match Student" button on the nav bar opens the correct oage
def test_goToMatchStudentPage():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    match_student_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[2]/a')
    
    #Upload Data button is clicked
    match_student_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Match Student Page"

    driver.quit()


#test if clicking the "Settings" button on the nav bar opens the correct oage
def test_goToSettingsPage():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    settings_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[4]/a')
    
    #Upload Data button is clicked
    settings_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Settings Page"

    driver.quit()


#test if student data is uploaded successfully
def test_uploadStudentData():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_data_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[1]/a')
    
    #Upload Data button is clicked
    upload_data_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Upload Data Page"

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
    match_student_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[2]/a')
    
    #Upload Data button is clicked
    match_student_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title2 = driver.title
    assert target_title2 == "DevOps Team 5 Match Student Page"

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
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_data_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[1]/a')
    
    #Upload Data button is clicked
    upload_data_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Upload Data Page"

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
    match_student_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[2]/a')
    
    #Upload Data button is clicked
    match_student_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title2 = driver.title
    assert target_title2 == "DevOps Team 5 Match Student Page"

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

#test if company data is uploaded successfully
def test_uploadCompanyData():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_data_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[1]/a')
    
    #Upload Data button is clicked
    upload_data_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Upload Data Page"

    driver.implicitly_wait(0.5)

    #find the upload file button and click it
    upload_student_data_button = driver.find_element(by=By.ID, value="upload-company-data-file")
    
    #Upload Student Data button is clicked
    upload_student_data_button.send_keys(companyDataFileName)

    companyData = getCompanyInfo(companyDataFileName)

    #check if the right file is uploaded
    file_upload_message = driver.find_element(by=By.ID, value="upload-company-data-file-message").text
    assert file_upload_message + "File Uploaded:" + companyDataFileName

    driver.implicitly_wait(2)

    #find the button to enter Upload Data page, subdue to naming changes
    match_student_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[2]/a')
    
    #Upload Data button is clicked
    match_student_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title2 = driver.title
    assert target_title2 == "DevOps Team 5 Match Student Page"

    driver.implicitly_wait(0.5)

    driver.quit()
    
