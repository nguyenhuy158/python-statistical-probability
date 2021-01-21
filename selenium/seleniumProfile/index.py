from selenium import webdriver

# load profile
options = webdriver.ChromeOptions()
# options.add_argument("no-sandbox")
# options.add_argument("--disable-gpu")
# options.add_argument("--window-size=500,500")
# options.add_argument("--disable-dev-shm-usage")
options.add_argument('--user-data-dir=C:/Users/Python/PycharmProjects/PythonTool/seleniumProfile/profile')
options.add_argument('--profile-directory=profile')
driver = webdriver.Chrome(options=options)

url = 'https://youtube.com'
driver.get(url)
