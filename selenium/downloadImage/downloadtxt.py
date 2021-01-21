
# Import libraries
import requests
import urllib.request, urllib.error, urllib.error
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'http://web.mta.info/developers/turnstile.html'
key = 'picture'
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object¶
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
line_count = 1  # variable to track what line you are on
for one_a_tag in soup.findAll('a'):  # 'a' tags are for links
    if line_count >= 38:  # code for text files starts at line 36
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/' + link
        urllib.request.urlretrieve(download_url, key + str(line_count) + ".txt")
        time.sleep(1)  # pause the code for a sec
    #add 1 for next line
    line_count += 1
    print(line_count)
