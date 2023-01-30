from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os.path
import main
import Email
import database_crud as db

def test_home_url():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.get("http://127.0.0.1:5221/Main")

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "DevOps Team 5 Home Page"


def test_upload_data_url():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.get("http://127.0.0.1:5221/Upload_Data")

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "DevOps Team 5 Upload Data Page"

def test_match_student_url():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.get("http://127.0.0.1:5221/Match_Student")

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "DevOps Team 5 Match Student Page"

def test_prepare_email_url():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.get("http://127.0.0.1:5221/Prepare_Email")

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "DevOps Team 5 Prepare Email Page"

def test_settings_url():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    
    driver.get("http://127.0.0.1:5221/Settings")

    # Check that its at NLB Home Page
    title = driver.title
    assert title == "DevOps Team 5 Settings Page"

def test_check_path_exists():
    check = main.check_path_exists('C:\\Windows')
    assert check == True

def test_email_function():
    Email.create_email("s10194152@connect.np.edu.sg", "Tan Jun Jie", "29/1/2023", "29/7/2023", "C:\\")

    assert os.path.exists("C:\\Tan Jun Jie Internship Email.msg") == True
    
def test_create_table():
    assert db.create_table() == ('exist',)