import random
from time import sleep
from selenium import webdriver
from driverBasic import captureFullScreenshot

def main(save):
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSe64mAql2IXBXbx8Cq1-oBpOZIoQJ1PMsmIofvCStYDQ7NdIw/viewform'
    driver = webdriver.Firefox()
    driver.get(url)

    # start
    input = driver.find_element_by_css_selector('.quantumWizTextinputPapertextareaInput')
    input.location_once_scrolled_into_view
    input.send_keys('.')

    input = driver.find_element_by_css_selector('.quantumWizTextinputPaperinputInput')
    input.location_once_scrolled_into_view
    input.send_keys('.')

    allQuestion = driver.find_elements_by_class_name('freebirdFormviewerComponentsQuestionBaseRoot')

    for question in allQuestion:
        count = 0
        try:
            count = question.find_elements_by_class_name('appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle')
        except:
            pass

        if len(count):
            key = random.randint(1, len(count))
            count[key - 1].click()
            sleep(3)

    #     continue
    driver.find_element_by_css_selector('.appsMaterialWizButtonPaperbuttonLabel').click()
    sleep(3)

    allQuestion = driver.find_elements_by_class_name('freebirdFormviewerComponentsQuestionBaseRoot')

    for question in allQuestion:
        keys = question.find_elements_by_class_name('appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle')
        key = random.randint(1, len(keys) - 1)
        keys[key - 1].click()
        sleep(2)

    #     continue
    driver.find_element_by_css_selector(
        'div.appsMaterialWizButtonEl:nth-child(2) > span:nth-child(3) > span:nth-child(1)').click()
    sleep(2)

    #     end
    driver.find_element_by_css_selector('div.appsMaterialWizButtonEl:nth-child(2) > span:nth-child(3)').click()
    sleep(1)
    captureFullScreenshot(driver, f'web_screenshot{save}.png')
    driver.close()


if __name__ == "__main__":
    for i in range(1, 100):
        main(i)
        print(i)
