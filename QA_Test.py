import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#set site's localhost IP Address and port, subdue to changes
global siteIPAddress, studentDataFileName
siteIPAddress = "http://127.0.0.1:5221"
studentDataFileName = "studentData.csv"

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
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_button = driver.find_element("xpath",'/html/body/header/div/strong/nav/ul/li[1]/a')
    
    
    #Upload Data button is clicked
    upload_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Upload Data Page"

    driver.quit()

