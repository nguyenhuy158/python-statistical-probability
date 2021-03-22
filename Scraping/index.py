import requests
from bs4 import BeautifulSoup
import re

# myset = set()
# with open('link.txt') as fi:
#     lines = fi.read().split()
#     for line in lines:
#         myset.add(line)
# print(myset)


# url = 'https://www.tutorialbar.com/'
# resoure = requests.get(url)
# print(resoure)
# soup = BeautifulSoup(resoure.text, 'html.parser')

myset = set()
with open('link.txt') as fi:
    lines = fi.read().split()
    for line in lines:
        myset.add(line)
# print(myset)
print("read done")

url = 'https://www.tutorialbar.com/'
from selenium import webdriver
import time
driver = webdriver.Chrome('D:/OneDrive - cloudor/Documents/Dev/chrome driver/chromedriver.exe')
driver.get(url)
n_scrolls = 10
for j in range(0, n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

source = driver.page_source
soup = BeautifulSoup(source, 'html.parser')
driver.quit()


def getLink(url):
    rs = requests.get(url);
    soup = BeautifulSoup(rs.text, 'html.parser')

    btn = soup.find('a', class_='btn_offer_block re_track_btn')
    link = re.findall('https://www.udemy.com\S{1,}\"', str(btn))

#     print(str(link)[2:-3])
    link = str(link)[2:-3]
    return link


print(len(soup.find_all(class_='mb15 mt0 font110 mobfont100 fontnormal lineheight20')))

with open('today.txt', mode='w') as fi:
    for e in soup.find_all(class_='mb15 mt0 font110 mobfont100 fontnormal lineheight20'):
        #     print(e.prettify())
        reg = re.findall('https://www.tutorialbar.com\S{1,}\/', str(e))
        #     print(''.join(reg))

        link = getLink(''.join(reg))

        if link not in myset:
            print(link)
            myset.add(link)
            fi.writelines('{}\n'.format(link))


with open('link.txt', mode='w') as fi:
    for st in myset:
        print(st)
        fi.writelines('{}\n'.format(st))
