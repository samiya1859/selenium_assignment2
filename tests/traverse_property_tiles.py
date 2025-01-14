import random
import logging
from selenium.webdriver.common.by import By
from utils.locator_reader import read_locators


def get_random_property_tiles(driver, num_tiles=10):
    """
    Selects random property tiles from the landing page.
    
    Args:
    driver: WebDriver instance
    num_tiles (int): Number of random tiles to select (default is 10).
    
    Returns:
    List of WebElements representing the randomly selected property tiles by sorted.
    """
    try:
        locators = read_locators()
        tiles_locator = locators.get("property_tile")
        all_tiles = driver.find_elements(By.XPATH, tiles_locator)
        
        if len(all_tiles) < num_tiles:
            num_tiles = len(all_tiles) 
        
        selected_tiles = random.sample(all_tiles, num_tiles)
         # Get sorted indices of the selected tiles
        sorted_indices = sorted([all_tiles.index(tile) for tile in selected_tiles])
        
        # Debugging: Print or log the selected tile indices
        logging.info(f"Total tiles found: {len(all_tiles)}")
        logging.info(f"Selected tile indices: {[all_tiles.index(tile) for tile in selected_tiles]}")
        logging.info(f"Selected tile indices: {sorted_indices}")

        return sorted_indices

    except Exception as e:
        logging.error(f"Error selecting random property tiles: {e}")
        return []