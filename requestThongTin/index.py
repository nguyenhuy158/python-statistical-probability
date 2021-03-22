import requests
import json

nameCountry = input('Enter name country: ')
r = requests.get(f'https://restcountries.eu/rest/v2/name/{nameCountry}')

if r.status_code == 200:
	print('finish!!!')

	# source = r.text[1:-1]
	# print(source)

	# myJson = json.loads(source)

	# print(myJson["name"])
	# print(myJson["capital"])

	with open(f'{nameCountry}.json', 'w', encoding="utf-8") as fi:
		fi.write(r.text[1:-1])

	with open(f'{nameCountry}.json', encoding="utf-8") as fi:
		myJson = json.load(fi)
	print(myJson["name"])
	print(myJson["capital"])
else:
	print('error')