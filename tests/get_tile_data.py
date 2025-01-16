import logging
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utils.locator_reader import read_locators

def extract_price(price_data):
    return price_data.replace("From ", "").strip()

def get_tile_data(driver, tile_element):
    """
    Extracts data from a single property tile.

    Args:
    driver: WebDriver instance (not currently used but reserved for future use)
    tile_element: The WebElement representing the tile

    Returns:
    A dictionary containing the extracted tile data.
    """
    tile_data = {
        'title': 'N/A',
        'price': 'N/A',
        'type': 'N/A',
        'rating': 'N/A',
        'reviews': 'N/A'
    }

    try:
        # Read locators from Excel
        locators = read_locators()

        # Extract data based on the locators
        if title_locator := locators.get("title"):
            try:
                tile_data['title'] = tile_element.find_element(By.XPATH, title_locator).text
            except NoSuchElementException:
                logging.error("Title not found, setting to 'N/A'")

        if price_locator := locators.get("price"):
            try:
                raw_price = tile_element.find_element(By.XPATH, price_locator).text
                tile_data['price'] = extract_price(raw_price)
                
            except NoSuchElementException:
                logging.error("Price not found, setting to 'N/A'")

        if type_locator := locators.get("type"):
            try:
                tile_data['type'] = tile_element.find_element(By.XPATH, type_locator).text
            except NoSuchElementException:
                logging.error("Type not found, setting to 'N/A'")

        if rating_locator := locators.get("rating"):
            try:
                tile_data['rating'] = tile_element.find_element(By.XPATH, rating_locator).text
            except NoSuchElementException:
                logging.error("Rating not found, setting to 'N/A'")

        if reviews_locator := locators.get("review"):
            try:
                tile_data['reviews'] = tile_element.find_element(By.XPATH, reviews_locator).text
            except NoSuchElementException:
                logging.error("Reviews not found, setting to 'N/A'")

        return tile_data

    except Exception as e:
        logging.error(f"Error extracting data from tile: {e}")
        return tile_data
