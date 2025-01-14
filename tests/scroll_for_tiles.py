from utils.locator_reader import read_locators
import time
import logging
from selenium.webdriver.common.by import By

def traverse_random_tiles(driver, sorted_tile_indices,  scroll_time=2):
    """
    Traverses through the selected random property tiles one by one.

    Args:
    driver: WebDriver instance
    sorted_tile_indices (list): Sorted list of indices of the selected property tiles.
    tiles_locator (str): XPath of the property tiles.
    scroll_time (int): Time to wait (in seconds) while scrolling to each tile.
    """
    try :
        locators = read_locators()
        tiles_locator = locators.get("property_tile")
        all_tiles = driver.find_elements(By.XPATH, tiles_locator)

        for index in sorted_tile_indices:
            # Get the current tile based on the sorted index
            tile = all_tiles[index]

            # Scroll the window to the selected tile
            driver.execute_script("arguments[0].scrollIntoView();", tile)
            time.sleep(scroll_time)  # Wait for a short time to visualize the scroll

            # Log the traversal
            logging.info(f"Traversing to tile {index + 1}: {tile.text[:50]}...")  
            
    except Exception as e:
        logging.error(f"Error during tile traversal: {e}")