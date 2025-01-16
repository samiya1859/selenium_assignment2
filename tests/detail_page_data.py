from selenium.webdriver.common.by import By
import time
from utils.locator_reader import read_locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import logging
import re


def extract_type(data_type):
    match = re.search(r'Check (\w+) Availability', data_type)
    if match:
        return match.group(1)
    return data_type

def extract_title(data_type):
    # Split the string at " | " and return the first part
    cleaned_type = data_type.split(" | ")[0]
    return cleaned_type.strip()

def get_detail_data(driver):

    """Extracts property details from the new tab."""

    detail_data = {
        'title': 'N/A',
        'price': 'N/A',
        'type': 'N/A',
        'rating': 'N/A',
        'reviews': 'N/A'
    }

    try:
        locators = read_locators()

        detail_container = locators.get("detail_container")
        # print("detail container : ",detail_container)

        detail_box = WebDriverWait(driver,20).until(
            EC.visibility_of_element_located((By.XPATH,detail_container))
        )


        title_locator = locators.get("detail_title")
        if title_locator:
            try:
                raw_title = detail_box.find_element(By.XPATH, title_locator).text
                detail_data['title'] = extract_title(raw_title)

            except NoSuchElementException:
                logging.error("Title not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map title is missing.")

        price_locator = locators.get("detail_price")
        if price_locator:
            try:
                detail_data['price'] = detail_box.find_element(By.XPATH, price_locator).text
            except NoSuchElementException:
                logging.error("Price not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map price is missing.")

        type_locator = locators.get("detail_type")
        if type_locator:
            try:
                raw_type = detail_box.find_element(By.XPATH, type_locator).text
                detail_data['type']=extract_type(raw_type)
            except NoSuchElementException:
                logging.error("Type not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map type is missing.")

        rating_locator = locators.get("detail_rating")
        if rating_locator:
            try:
                detail_data['rating'] = detail_box.find_element(By.XPATH, rating_locator).text
            except NoSuchElementException:
                logging.error("Rating not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map rating is missing.")

        reviews_locator = locators.get("detail_review")
        if reviews_locator:
            try:
                detail_data['reviews'] = detail_box.find_element(By.XPATH, reviews_locator).text
            except NoSuchElementException:
                logging.error("Reviews not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map reviews is missing.")
            
        

    except Exception as e:
        logging.error(f"Error extracting data from detail page: {e}")

    return detail_data
   