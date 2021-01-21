import requests
import urllib.error
import urllib.parse
import urllib.request
import time


from bs4 import BeautifulSoup
import os


def getUrlFromData():
    fi = open(
        r'c:\Users\Python\Desktop\code\downloadImage\getImgWallpaperscraft\url.txt', mode='r')
    url = fi.read()
    fi.close()
    return url


def getSource(url):
    requestsPage = requests.get(url)
    sourcePage = BeautifulSoup(requestsPage.text, "html.parser")
    return sourcePage


def returnUrlAllImg(sourcePage, heart01, heart02, className):
    list = []
    for child in sourcePage.findAll(heart01, {"class": className}):
        list.append(url_origin + str(child[heart02]))

    return list


def returnOneLink(sourcePage, heart01, heart02, className):
    link = ''
    for child in sourcePage.findAll(heart01, {"class": className}):
        link = str(child[heart02])
    return link


def writeData(data):
    fo = open('data.txt', mode='wb')
    print(data + '\n')
    fo.close()


def getName(url):
    childUrl = url.split('/')
    return childUrl[-1]


def downloadImgUrl(url):
    urllib.request.urlretrieve(url, r'./Img/' + getName(url))


def downloadOnePage(url):
    global countImg
    sourcePage = getSource(url)

    listLinkAllImg = returnUrlAllImg(
        sourcePage, 'a', 'href', 'wallpapers__link')
    print('getAllLink')
    listSourceImg = []
    for e in listLinkAllImg:
        listSourceImg.append(getSource(e))
    print('done')
    for e in listSourceImg:
        linkChildImg = returnOneLink(e, 'a', 'href', 'JS-Popup')
        print(str(countImg) + '-->' + getName(linkChildImg))
        downloadImgUrl(linkChildImg)
        countImg += 1


url = getUrlFromData()
url_origin = r'https://wallpaperscraft.com'
list_url = url.split('\n')

countImg = 1
for e in list_url:
    downloadOnePage(e)

print('sum:= ' + str(countImg))
