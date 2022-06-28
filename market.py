import requests
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver import Chrome
import pandas as pd


browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/selenium/chromedriver')
data = []
api = ['პური', 'შაქარი', 'ზეთი', 'ყავა%20ნალექიანი', 'მარილიანი%20ჩხირი', 'მზესუმზირა', 'ჩაი', 'ენერგეტიკული', 'ჩიფსი', 'წვენი', 'შოკოლადი', 'სასმელი', 'ლუდი', 'ღვინო']

for p in api:

	url = 'https://2nabiji.ge/ge/search?searchText='+str(p)

	browser.get(url)
	
	sleep(3)

	soup = BeautifulSoup(browser.page_source,'html.parser')
	data_info = soup.find('div', 'Layout_contentWrapper__2kQSf').find('main', class_='fit').find('div','infinite-scroll-component__outerdiv').find('div', 'Search_search__result__3gGsu')
	el_len = len(data_info.findAll('div', 'ProductCard_container__1jtJF'))
	

	for i in range(0, el_len):
		
		data_sourse = data_info.findAll('div', 'ProductCard_container__1jtJF')[i]
		
		tmp_name = data_sourse.find('div', class_='ProductCard_productInfo__21mxE')
		name = tmp_name.find('div', class_='ProductCard_title__rzbSG').text.strip()
		price = data_info.findAll('div', 'ProductCard_container__1jtJF')[i].find('div', class_='ProductCard_productInfo__price__2Ys9W').find('span').text.strip()
		
		
		
		data.append([name, price])
		

headers = ['name','price']

df = pd.DataFrame(data, columns = headers)

df.to_csv('/home/kali/market_data.csv', sep = ',', encoding= 'utf8')
	
		











































	
# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")
	
	
