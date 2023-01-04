import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as chrome_service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\\Users\\FL_LPT-373\\Downloads\\chromedriver_win32\\chromedriver.exe")
# LAUNCHING BROWSER
def login():
    # c_service = chrome_service("Drivers/chromedriver.exe")

    driver.maximize_window()
    driver.get("https://www.irctc.co.in/nget/train-search")
    driver.implicitly_wait(10)
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[@aria-label='Click here to register your account with I.R.C.T.C.']").click()
    driver.find_element(By.XPATH, "//a[@class='ns-66tao-e-15 button']").click()
    driver.find_element(By.XPATH, "//input[@type='number']").send_keys(8332062227)
    driver.find_element(By.XPATH,"//button[@class='resusables__Button-ds85e6-1 styles__InputCTA-sc-1vnxfs1-2 fKuasZ']").click()
    time.sleep(5)
    captcha=driver.find_element(By.XPATH,"(//span[@class='ng-star-inserted'])[3]//img[@class='captcha-img']").text
    time.sleep(3)
    print("captcha is :",captcha)

    driver.find_element(By.XPATH,"//input[@formcontrolname='captcha']").send_keys(captcha)

    time.sleep(5)
    driver.find_element(By.XPATH,"//label[@for='otpLogin']").click()
    driver.find_element(By.XPATH,"(//button[@class='btn btn-primary'])[1]").click()
    driver.find_element(By.XPATH,"//button[@style='padding: 10px 14px;']").click()
    driver.find_element(By.XPATH,"//button[@style='padding: 10px 14px;']").click()
    driver.find_element(By.XPATH,"//label[@class='search_btn']").click()
def register():
    driver.find_element(By.XPATH, "//a[@aria-label='Click here to register your account with I.R.C.T.C.']").click()
    driver.find_element(By.XPATH,"//input[@id='userName']").send_keys("Dhruvansh1234")
    driver.find_element((By.XPATH,"//input[@id='usrPwd']")).send_keys("nani")
    driver.find_element(By.XPATH,"//input[@id='cnfUsrPwd']").send_keys("nani")
    driver.find_element(By.XPATH,"//div[@class='ng-tns-c65-14 ui-dropdown ui-widget ui-state-default ui-corner-all']").send_keys("English")
    driver.find_element(By.XPATH,"//span[@class='ng-tns-c65-15 ui-dropdown-label ui-inputtext ui-corner-all ui-placeholder ng-star-inserted']").send_keys("What is your pet name?")
    driver.find_element(By.XPATH,"//input[@formcontrolname='secAns']").send_keys("Nani")
    driver.find_element(By.XPATH,"//button[@label='Continue']").click()
def tickets():

    ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"//strong[text()='TRAINS']")).perform()
    driver.find_element(By.XPATH,"//span[text()='Book Ticket']").click()
    driver.find_element(By.XPATH,"//input[@role='searchbox']").send_keys("Hyderabad")
    driver.find_element(By.XPATH,"(//input[@role='searchbox'])[2]").send_keys("Delhi")
    driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
    driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("09/01/2023")
    driver.find_element(By.XPATH,"//span[@class='ui-dropdown-trigger-icon ui-clickable ng-tns-c65-36 pi "
                                 "pi-chevron-down']").click()
    driver.find_element(By.XPATH,"//span[text()='LOWER BERTH/SR.CITIZEN']").click()
    driver.find_element(By.XPATH,"//button[@label='Find Trains']").click()
login()
register()
tickets()