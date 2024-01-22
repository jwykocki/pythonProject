import configparser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import offer.offer as offer_dto

config = configparser.ConfigParser()
config.read('config.ini')
tech = config.get('scrapper', 'tech')
location = config.get('scrapper', 'location')

JUST_JOIN_IT_URL = "https://justjoin.it/"

def get_offers_from_website():
    driver = webdriver.Chrome()
    url = JUST_JOIN_IT_URL + location + "/" + tech

    driver.get(url)
    wait = WebDriverWait(driver, 10)
    main_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="virtuoso-item-list"]')))
    items = main_container.find_elements(By.CSS_SELECTOR, 'div[data-index]')
    offers_list = []
    for item in items:
        offer_url = item.find_element(By.CSS_SELECTOR, 'a.css-4lqp8g').get_attribute('href')
        offer = item.find_element(By.CSS_SELECTOR, 'div.MuiBox-root.css-6vg4fr')
        title = offer.find_element(By.CSS_SELECTOR, 'h2.css-16gpjqw').text
        salary = offer.find_element(By.CSS_SELECTOR, 'div.css-1b2ga3v').text
        company = item.find_element(By.CSS_SELECTOR, 'div.css-ldh1c9').find_element(By.TAG_NAME, 'span').text
        offers_list.append(offer_dto.Offer(offer_url, title, company, salary))
    print(offers_list)
    return offers_list
