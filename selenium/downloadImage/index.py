
# Import libraries
import requests
import urllib.request
import urllib.error
import urllib.error
import time
from bs4 import BeautifulSoup
import os

# ======================


def getNameFile(url):
    childUrl = url.split('/')
    return childUrl[-1]


# ======================
# Set the URL you want to webscrape from
read_url = open('url.txt', mode='r')
url = read_url.read()
read_url.close()
key = r'./download2/'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
fi = open('link_page_picture.txt', mode='w', encoding="utf-8")
soup = BeautifulSoup(response.text, "html.parser")

count = 0
for a in soup.findAll('a', {"class": "thumb-wrp"}):
    count += 1
print(count)
count = 1
for a in soup.findAll('a', {"class": "thumb-wrp"}):
    link_page_picture = r'https://www.wallpaperup.com/' + a['href']
    response_download_one_picture = requests.get(link_page_picture)

    soup_one_page = BeautifulSoup(response_download_one_picture.text, "html.parser")
    for link in soup_one_page.findAll('img', {"class": "thumb black full zoomable magnified"}):
            link_download = link['data-original']
            urllib.request.urlretrieve(link_download, key + getNameFile(link_download))
            print(str(link_download))
    print(count)
    count += 1
fi.close
