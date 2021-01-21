
# Import libraries
import requests
import urllib.request
import urllib.error
import urllib.error
import time
from bs4 import BeautifulSoup
import os
# Set the URL you want to webscrape from
url = 'https://unsplash.com/s/photos/animal'
key = r'./download1/picture'
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
fi = open('data.txt', mode='w', encoding="utf-8")
soup = BeautifulSoup(response.text, "html.parser")
for a in soup.findAll('img'):
    fi.write(str(a['src']) + "\n")
fi.close


number = 1
for one_a_tag in soup.findAll('img'):  # 'a' tags are for links
    url_download = one_a_tag['src']
    urllib.request.urlretrieve(url_download,key+str(number)+".png")
    number += 1
    time.sleep(0.5)
    
print(number)
