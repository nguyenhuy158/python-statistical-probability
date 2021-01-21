import urllib.request
# url = r'https://images.unsplash.com/photo-1541565726581-3423fce9c139?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=253&q=80'


url = r'https://www.wallpaperup.com/uploads/wallpapers/2017/04/22/1086857/48df69b50d7601215c6509cb7bd6ab69-700.jpg'
urllib.request.urlretrieve(url, "local.jpg")
