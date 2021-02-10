import requests
import sqlite3
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def setup_db():
    conn = sqlite3.connect('url_from_search.db')
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS url_from_search ( 
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Title TEXT,
                    Url TEXT
                    )""")
    sample_data = [
        ('Title_1', 'Url_1'),
        ('Title_2', 'Url_2'),
    ]
    cursor.executemany('INSERT INTO url_from_search (Title, Url) VALUES(?, ?)', sample_data)
    yield conn



@pytest.fixture
def browser():
    firefox_options = Options()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_connection(setup_db):
    # Test to make sure that there are 2 items in the database
    cursor = setup_db
    assert len(list(cursor.execute('SELECT * FROM url_from_search'))) == 2


def test_search(browser):
    browser.get("https://www.google.com/")
    text = 'qwerty'
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)
    urls_result = browser.find_elements_by_class_name('yuRUbf')
    assert len(urls_result) > 0
    xpath = f"//h3[@class='LC20lb DKV0Md']//*[contains(text(), text)]"
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == text

