from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

driver = webdriver.Firefox()

driver.get('https://youtube.com')

wait = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(By.CSS_SELECTOR, 'input.ytd-searchbox'))
time.sleep(0.5)
send = driver.find_element(By.CSS_SELECTOR, 'input.ytd-searchbox').send_keys('tao lao' + Keys.RETURN)