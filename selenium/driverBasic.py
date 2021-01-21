from selenium import webdriver
from selenium.webdriver.common.by import By


def openWeb(url):
    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": r"C:\Users\Python\PycharmProjects\PythonTool\selenium\downloadFile",
                   "safebrowsing.enabled": "false"}
    options.add_experimental_option("prefs", preferences)

    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    return driver


def clickByCss(driver, css):
    driver.find_element(By.CSS_SELECTOR, css).click()


def clickByXpath(driver, xpath):
    driver.find_element(By.XPATH, xpath).click()


def sentTextByCss(driver, css, text):
    driver.find_element(By.CSS_SELECTOR, css).send_keys(text)


def captureFullScreenshot(driver, name):
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    driver.set_window_size(S('Width'), S(
        'Height'))  # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot(name)


def main():
    openWeb('')


if __name__ == "__main__":
    main()
