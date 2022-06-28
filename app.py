import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

# url = 'https://www.kinopoisk.ru/lists/movies/top250/?page={p}'
#
# r = requests.get(url)
# r.text
#
# soup = BeautifulSoup(r.text, "html.parser")
#
# link = "https://www.kinopoisk.ru/"+soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').get('href')
# name_ru = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
# name_us = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
# country = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text
# rate = soup.find('div', class_='styles_root__ti07r').find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg').text
#


data = []

for p in range(1, 6):

	print(p)
	url = 'https://www.kinopoisk.ru/lists/movies/top250/?page={p}'
	r = requests.get(url)
	sleep(15)

	soup = BeautifulSoup(r.text, "html.parser")

	films = soup.findAll('div', class_='styles_root__ti07r')


	for films in films:

		links = "https://www.kinopoisk.ru/" + films.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
		# name_ru=films.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZstyles_activeMovieTittle__kJdJj').text
		name_us=films.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
		country=films.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text
		rate=films.find('span', class_='styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg').text

		data.append([links, name_us, country, rate])


headers = ['links', 'name_us', 'country', 'rate']

df = pd.DataFrame(data, columns=headers)
df.to_csv('/home/kali/data.csv', sep=';', encoding='utf8')


