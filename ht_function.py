
def ht_function(arg):

    from selenium import webdriver
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait as wait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    from bs4 import BeautifulSoup
    from time import sleep
    from tqdm import tqdm
    import pandas as pd

    ht_data = []

    url = arg
    browser = webdriver.Chrome(executable_path='/home/kali/PycharmProjects/selenium/chromedriver')
    browser.get(url)

    browser.find_element_by_xpath('//*[@id="offers-part"]')
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    data = soup.findAll('div', class_='col-xl-3 col-lg-4 col-md-3 mb-4')

    el_len = len(data)

    for i in range(0, el_len):

        ht_tmp = ht_name = data[i].find('div', class_='suggestion_box').find('div', class_='suggest_items').find('div',
                                                                                                                 class_='suggestion_information')

        ht_lnk = ht_tmp.find('a').get('href')

        ht_name = ht_tmp.find('a').find('h3', class_='company_title').text.strip()

        ht_desc = ht_tmp.find('div', class_='suggestion_txt_title').text.strip()

        ht_price_old = ht_tmp.find('div', class_='secondary_info d-flex align-items-center justify-content-between').find(
            'div', class_='save_total_ d-flex flex-column').find('span', class_='old_price_ mb-0').text.strip()

        hr_price_new = ht_tmp.find('div', class_='secondary_info d-flex align-items-center justify-content-between').find(
            'div', class_='save_total_ d-flex flex-column').find('div', class_='new_price').text.strip()

        try:
            hr_raiting = ht_tmp.find('div', class_='secondary_info d-flex align-items-center justify-content-between').find(
                'div', class_='d-flex flex-column align-items-center').find('div', class_='rating').find('span',
                                                                                                         class_='rating_num').text.strip()

        except:
            hr_raiting = '0'

        ht_save = ht_tmp.find('div', class_='secondary_info d-flex align-items-center justify-content-between').find('div',
                                                                                                                     class_='d-flex flex-column align-items-center').find(
            'div', class_='save_').find('p', class_='save_p').find('span').text.strip()

        ht_data.append([ht_name, ht_desc, ht_price_old, hr_price_new, hr_raiting, ht_save])

    print(ht_data)

    headers = ['ht_name', 'ht_desc', 'ht_price_old', 'hr_price_new', 'hr_raiting', 'ht_save']

    try:
        df = pd.DataFrame(ht_data, columns=headers)
        df.to_csv('/home/kali/ht_data.csv', sep=';', encoding='utf8')
        print('ht_data CREATED..')
    except:
        print('incoreect Value..!')















