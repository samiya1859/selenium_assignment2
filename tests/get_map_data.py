from selenium.webdriver.common.by import By
import time
from utils.locator_reader import read_locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import logging

def extract_map_data(driver):
    """
    Extracts data from the map info window after the map icon is clicked.

    Args:
    driver: WebDriver instance
    tile : the selected tile element
    
    Returns:
    dict: A dictionary containing the extracted map data (e.g., title, price, rating).
    """
    map_data = {
        'title': 'N/A',
        'price': 'N/A',
        'type': 'N/A',
        'rating': 'N/A',
        'reviews': 'N/A'
    }

    

    try:
        locators = read_locators()

        map_info_locator = locators.get("map_box")
        print("map-box",map_info_locator)
        map_info_box = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, map_info_locator))
        )

        
        # Extract data based on the locators
        title_locator = locators.get("map_title")
        if title_locator:
            try:
                map_data['title'] = map_info_box.find_element(By.XPATH, title_locator).text
            except NoSuchElementException:
                logging.error("Title not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map title is missing.")

        price_locator = locators.get("map_price")
        if price_locator:
            try:
                map_data['price'] = map_info_box.find_element(By.XPATH, price_locator).text
            except NoSuchElementException:
                logging.error("Price not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map price is missing.")

        type_locator = locators.get("map_type")
        if type_locator:
            try:
                map_data['type'] = map_info_box.find_element(By.XPATH, type_locator).text
            except NoSuchElementException:
                logging.error("Type not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map type is missing.")

        rating_locator = locators.get("map_rating")
        if rating_locator:
            try:
                map_data['rating'] = map_info_box.find_element(By.XPATH, rating_locator).text
            except NoSuchElementException:
                logging.error("Rating not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map rating is missing.")

        reviews_locator = locators.get("map_review")
        if reviews_locator:
            try:
                map_data['reviews'] = map_info_box.find_element(By.XPATH, reviews_locator).text
            except NoSuchElementException:
                logging.error("Reviews not found, setting to 'N/A'")
        else:
            logging.warning("Locator for map reviews is missing.")
            
        return map_data

    except Exception as e:
        logging.error(f"Error extracting data from map: {e}")
        return map_data



