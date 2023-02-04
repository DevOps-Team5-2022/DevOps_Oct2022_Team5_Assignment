from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager
import os.path
from os import environ
import main
import Email
import database_crud as db
import pandas as pd

chromeOption = options.Options()
for option in ['--headless','--disable-gpu','--window-size=1920,1200','--ignore-certificate-errors','--disable-extensions','--no-sandbox','--disable-dev-shm-usage']:
    chromeOption.add_argument(option)

driver = webdriver.Chrome(options = chromeOption)


def test_home_url():
    
    driver.get("http://127.0.0.1:5221/Main")

    # Check that its at Home Page
    assert driver.title == "DevOps Team 5 Home Page"

def test_upload_data_url():
    
    driver.get("http://127.0.0.1:5221/Upload_Data")

    # Check that its at Upload Data Page
    assert driver.title == "DevOps Team 5 Upload Data Page"

def test_match_student_url():
 
    driver.get("http://127.0.0.1:5221/Match_Student")

    # Check that its at Match Student Page
    assert driver.title == "DevOps Team 5 Match Student Page"

def test_prepare_email_url(): 
    driver.get("http://127.0.0.1:5221/Prepare_Email")

    # Check that its at Prepare Email Page
    assert driver.title == "DevOps Team 5 Prepare Email Page"

def test_settings_url():
    driver.get("http://127.0.0.1:5221/Settings")

    # Check that its at Settings Page
    assert driver.title == "DevOps Team 5 Settings Page"

def test_create_email_function():
    result = Email.create_email("s10194152@connect.np.edu.sg", "Tan Jun Jie", "29/1/2023", "29/7/2023")

    assert result.recipients[0].display_name == 'Tan Jun Jie'
    assert result.recipients[0].email_address == 's10194152@connect.np.edu.sg'
    assert result.subject == "Internship Response to Internship Request"
    assert result.body == "Dear Tan Jun Jie,\nKindly find attached our students resume for the 2023" \
                   " semester Internship in response to your job description which you have submitted to us." + \
                   "\nWe look forward to your favorable response and to working with your company for the upcoming internship period 29/1/2023 to 29/7/2023"
    
def test_create_table():
    assert db.create_table() == ('exist',)

def test_insert_record():
    assert db.insert_record() == "inserted"

def test_update_record():
    assert db.update_record() == "true"

def test_delete_record():
    assert db.delete_record() == "false"

def test_delete_table():
    assert db.delete_table() == ('nonexist',)

def test_successful_upload_student_data():
    studentTestData = {'StudentID': ["S87654321A"], 'Name': ['Test1'], 'Preference': ['Testing'], 'Status': ['Unassigned']}
    studentTestDataframe = pd.DataFrame(data = studentTestData)
    result = main.upload_data_func(studentTestDataframe, 'student')
    assert result == 'success'

def test_successful_upload_company_data():
    companyTestData = {'CompanyName': ["Test Company"], 'JobRole': ['Tester'], 'CompanyContact': ['Test User'], 'Email': ['test@gmail.com']}
    companyTestDataframe = pd.DataFrame(data = companyTestData)
    result = main.upload_data_func(companyTestDataframe, 'company')
    assert result == 'success'


