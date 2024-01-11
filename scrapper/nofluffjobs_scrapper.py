from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import offer.offer as offer_dto


def get_offers_from_website():
    driver = webdriver.Chrome()
    driver.get("https://nofluffjobs.com/pl/Java?page=1")
    wait = WebDriverWait(driver, 10)
    main_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list-container')))
    job_offer_elements = main_container.find_elements(By.CLASS_NAME, 'posting-list-item--backend')
    offers_list = []
    for job_offer_element in job_offer_elements:
        offer_url = job_offer_element.get_attribute('href')
        title = job_offer_element.find_element(By.CLASS_NAME, 'posting-title__position').text
        company = job_offer_element.find_element(By.CLASS_NAME, 'company-name').text
        salary = job_offer_element.find_element(By.CLASS_NAME, 'text-truncate.badgy.salary').text
        offers_list.append(offer_dto.Offer(offer_url, title, company, salary))
    return offers_list
if __name__ == '__main__':
    offers = get_offers_from_website()
    print(offers)