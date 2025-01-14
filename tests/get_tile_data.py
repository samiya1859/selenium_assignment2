import logging
from selenium.webdriver.common.by import By
from utils.locator_reader import read_locators


def get_tile_data(driver, tile_element):
    """
    Extracts data from a single property tile.
    
    Args:
    driver: WebDriver instance
    tile_element: The WebElement representing the tile
    
    Returns:
    A dictionary containing the extracted tile data.
    """
    tile_data = {}

    try:
        # Read locators from Excel
        locators = read_locators()
        
        title_locator = locators.get("title")
        price_locator = locators.get("price")
        type_locator = locators.get("type")
        rating_locator = locators.get("rating")
        reviews_locator = locators.get("reviews")

        if title_locator:
            title = tile_element.find_element(By.XPATH,title_locator).text
            tile_data['title'] = title

        if price_locator:
            price = tile_element.find_element(By.XPATH, price_locator).text
            tile_data['price'] = price

        if type_locator:
            type_value = tile_element.find_element(By.XPATH, type_locator).text
            tile_data['type'] = type_value

        if rating_locator:
            rating = tile_element.find_element(By.XPATH, rating_locator).text
            tile_data['rating'] = rating

        if reviews_locator:
            reviews = tile_element.find_element(By.XPATH, reviews_locator).text
            tile_data['reviews'] = reviews

        return tile_data
    
    except Exception as e:
        logging.error(f"Error extracting data from tile: {e}")
        return {}



