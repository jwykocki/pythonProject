from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import offer.offer as offer_dto


def get_offers_from_website():
    driver = webdriver.Chrome()
    driver.get("https://justjoin.it/")
    wait = WebDriverWait(driver, 10)
    main_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-test-id="virtuoso-item-list"]')))
    items = main_container.find_elements(By.CSS_SELECTOR, 'div[data-index]')
    offers_list = []
    for item in items:
        offerUrl = item.find_element(By.CSS_SELECTOR, 'a.css-4lqp8g').get_attribute('href')
        offer = item.find_element(By.CSS_SELECTOR, 'div.MuiBox-root.css-6vg4fr')
        title = offer.find_element(By.CSS_SELECTOR, 'h2.css-16gpjqw')
        salary = offer.find_element(By.CSS_SELECTOR, 'div.css-1b2ga3v')
        company = item.find_element(By.CSS_SELECTOR, 'div.css-ldh1c9').find_element(By.TAG_NAME, 'span')
        offers_list.append(offer_dto.Offer(offerUrl, title.text, company.text, salary.text))
    return offers_list
