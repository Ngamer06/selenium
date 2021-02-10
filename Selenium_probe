from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import db_selenium as db


firefox_options = Options()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(options=firefox_options)
try:
    driver.get("https://www.google.com/")
    assert "Google" in driver.title
    elem = driver.find_element_by_name("q")
    text = 'qwert' #input ('Введите запрос для поиска: ')
    number_pages = 3#int(input ('Введите кол-во страниц для поиска: '))
    elem.send_keys(text)
    elem.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    db.create_db()
    page = 1
    while page <= number_pages:     
        print('Parse page ' + str(page))
        urls = driver.find_elements_by_class_name('yuRUbf')
        for url in urls:
            link = url.find_element_by_xpath('a').get_attribute('href')
            title = url.find_element_by_xpath('.//h3').text
            db.add_db(link, title)
        xpath = '/html/body/div[7]/div[2]/div[9]/div[2]/div/div[5]/div[2]/span[1]/div/table/tbody/tr/td[12]/a'
        driver.find_element_by_xpath(xpath).click()
        page +=1
    else:
        print('Parse is over')
finally:
    driver.close()
