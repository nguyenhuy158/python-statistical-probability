from time import sleep

from selenium import webdriver

# selecte element
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def clickVideo(url, time):
    driver = webdriver.Firefox(executable_path='geckodriver.exe')
    driver.get(url)
    sleep(1)

    # fullScreen = driver.find_elements(By.CLASS_NAME, 'yt-simple-endpoint.style-scope.ytd-video-renderer')
    # print(len(fullScreen))
    # for screen in fullScreen:
    #     print(screen.text)
    #     if screen.text == title:
    #         screen.click()
    #         break
    # driver.find_element(By.PARTIAL_LINK_TEXT, '## || Lễ tri ân').click()
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Hy Quaq').click()
    sleep(time)
    driver.close()


url = 'https://www.youtube.com/results?search_query=tri+an+tn2'
title = '## || Lễ tri ân - trưởng thành TT TN2 || 2017-2020'
# title = '#01 || Điểm danh nào TN2'
n = 2
for i in range(n):
    clickVideo(url, 10)
    sleep(2)
