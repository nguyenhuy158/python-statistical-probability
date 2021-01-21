
def getNameFile(url):
    childUrl = url.split('/')
    print(childUrl)
    return childUrl[-1]

url = r'https://www.wallpaperup.com/uploads/wallpapers/2017/04/22/1086857/48df69b50d7601215c6509cb7bd6ab69.jpg'

print(getNameFile(url))
