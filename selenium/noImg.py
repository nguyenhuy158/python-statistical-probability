from selenium import webdriver

chrome_option = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_option.add_experimental_option("prefs", prefs)
chrome_option.add_argument(
    "user-data-dir="+"profile"
)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://youtube.com")
