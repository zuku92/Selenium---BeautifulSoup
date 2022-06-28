import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

data = []
url = 'https://jobs.ge/?page=1&q=&cid=6&lid=&jid=1'

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

vk = soup.findAll('a', class_='vip')
el_len = (len(vk))


for p in range(1, el_len):
    try:
        lnk = "https://jobs.ge" + soup.find('div', class_='regularEntries').find('table').findAll('tr')[p].find('a', class_='vip').get('href')
        name = soup.find('div', class_='regularEntries').find('table').findAll('tr')[p].find('a', class_='vip').text
        date_start = soup.find('div', class_='regularEntries').find('table').findAll('tr')[p].findAll('td')[4].text.strip()
        date_end = soup.find('div', class_='regularEntries').find('table').findAll('tr')[p].findAll('td')[5].text.strip()
        date_valid = date_start + '-' + date_end
        company = soup.find('div', class_='regularEntries').find('table').findAll('tr')[p].findAll('td')[3].text.strip()

        data.append([lnk, name, company, date_valid])

    except:
        pass

headers = ['lnk', 'name', 'company', 'date_valid']
try:
    df = pd.DataFrame(data, columns=headers)
    df.to_csv('/home/kali/jobs_data.csv', sep=';', encoding='utf8')
    print('jobs_data CREATED..')
except:
    print('incoreect Value..!')

print(data)






