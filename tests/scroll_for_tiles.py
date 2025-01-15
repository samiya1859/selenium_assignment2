from utils.locator_reader import read_locators
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .get_tile_data import get_tile_data
from .click_map_icon import click_map_icon
from .get_map_data import extract_map_data
from .click_property_title import click_property_title_and_close_tab

def traverse_random_tiles(driver, sorted_tile_indices,  scroll_time=3):
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
        

        for index in sorted_tile_indices:
            # Get the current tile based on the sorted index
            tile_xpath = locators.get("tile_individual").format(index=index)
            # print(tile_xpath)
            # Get the current tile element using the dynamic XPath
            tile = driver.find_element(By.XPATH, tile_xpath)


            # Scroll the window to the selected tile
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", tile)

            time.sleep(scroll_time) 
            driver.execute_script("window.scrollBy(0, -100);")

            # Wait for the data to be visible before extracting it
            WebDriverWait(driver, 5).until(
                EC.visibility_of(tile)
            )

            tile_data = get_tile_data(driver,tile)
            time.sleep(2)
            click_map_icon(driver,tile)
            map_data = extract_map_data(driver)
            time.sleep(1)
            click_property_title_and_close_tab(driver,tile)
            time.sleep(1)





            # Print data for debugging
            logging.info(f"Data from tile {index}: {tile_data}")
            logging.info(f"Data from map {index}: {map_data}")
            

            # Clear the tile_data for next iteration
            tile_data.clear()
            map_data.clear()

           
            
    except Exception as e:
        logging.error(f"Error during tile traversal and data extraction: {e}")