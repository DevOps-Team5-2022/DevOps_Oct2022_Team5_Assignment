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

#test if clicking the "Upload Data" button on the nav bar opens the correct oage
def test_goToUploadDataPage():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get(siteIPAddress + "/Main")

    #checks if the home pahe is loaded
    title = driver.title
    assert title == "DevOps Team 5 Home Page"

    driver.implicitly_wait(0.5)

    #find the button to enter Upload Data page, subdue to naming changes
    upload_button = driver.find_element(By.id("upload-data-button"))
    
    
    #Upload Data button is clicked
    upload_button.click()

    driver.implicitly_wait(0.5)
    
    #checks if the Upload Data pahe is loaded
    target_title = driver.title
    assert target_title == "DevOps Team 5 Upload Data Page"

    driver.quit()

