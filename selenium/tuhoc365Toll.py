from time import sleep

from selenium import webdriver

# selecte element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

url = 'http://lp.tuhoc365.vn/tai-lieu-mien-phi/?c41713Le'
urlGmail = 'https://10minutemail.net/?lang=vi'

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get(urlGmail)
sleep(1)

# get email 10p
gmail = driver.find_element(By.ID, 'fe_text').get_attribute('value')
print(f"gmail : {gmail}")
# open web
sleep(2)
driver.get(url)
# send data
cellName = driver.find_element(By.ID, 'name')
cellName.clear()
cellName.send_keys('Tu hoc')

cellEmail = driver.find_element(By.ID, 'email')
cellEmail.clear()
cellEmail.send_keys(gmail)

# click button
sleep(1)
driver.find_element(By.ID, 'signup').click()
print('click done')





