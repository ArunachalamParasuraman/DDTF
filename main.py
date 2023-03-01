from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from locators import Test_Locators
from excel_functions import Arun_excel_function

Excel_file = "C:\\Users\\aruns\\Desktop\\DDF\\test_data.xlsx"
Sheet_number = 'Sheet1'
url = 'https://www.facebook.com'
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(url)
a = Arun_excel_function(Excel_file,Sheet_number)
rows = a.Row_Count()
for row in range(2,rows+1):
    username = a.Read_Data(row,6)
    password = a.Read_Data(row,7)
    driver.find_element(by=By.NAME,value=Test_Locators().Username_Locator).send_keys(username)
    driver.find_element(by=By.NAME,value=Test_Locators().Password_Locator).send_keys(password)
    driver.find_element(by=By.NAME,value=Test_Locators().SubmitButtonLocator).click()
    driver.implicitly_wait(10)
    if ('https://www.facebook.com/checkpoint/?next' in driver.current_url):
        print('Success : Test Success with username:{a}'.format(a = username))
        a.Write_Data(row,8,'TEST PASS')
        driver.back()
    elif('https://www.facebook.com' in driver.current_url):
        print('Failed : Test Failed with username:{a}'.format(a = username))
        a.Write_Data(row,8,'TEST FAIL')
        driver.back()
driver.quit()

