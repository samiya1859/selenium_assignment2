from utils.locator_reader import read_locators
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .get_tile_data import get_tile_data
from .click_map_icon import click_map_icon
from .get_map_data import extract_map_data
from .comaparing_datas import compare_data
from .click_property_title import click_property_title_and_close_tab

def traverse_random_tiles(driver, sorted_tile_indices, scroll_time=3):
    """
    Traverses through the selected random property tiles one by one.

    Args:
    driver: WebDriver instance
    sorted_tile_indices (list): Sorted list of indices of the selected property tiles.
    scroll_time (int): Time to wait (in seconds) while scrolling to each tile.
    """
    test_results = []
    try:
        locators = read_locators()

        for index in sorted_tile_indices:
            try:
                # Get the current tile based on the sorted index
                tile_xpath = locators.get("tile_individual").format(index=index)
                tile = driver.find_element(By.XPATH, tile_xpath)

                # Scroll to the tile
                driver.execute_script(
                    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", 
                    tile
                )
                time.sleep(scroll_time)  # Adjust as needed
                driver.execute_script("window.scrollBy(0, -100);")

                WebDriverWait(driver, 5).until(EC.visibility_of(tile))

                # Extract data from the tile, map, and detail page
                tile_data = get_tile_data(driver, tile)
                time.sleep(2)
                click_map_icon(driver, tile)
                map_data = extract_map_data(driver)
                time.sleep(1)
                detail_data = click_property_title_and_close_tab(driver, tile)
                time.sleep(1)

                # Log data
                logging.info(f"Data from tile {index}: {tile_data}")
                logging.info(f"Data from map {index}: {map_data}")
                logging.info(f"Data from detail page {index}: {detail_data}")

                compare_data_result = compare_data(tile_data,map_data,detail_data)

                test_results.append(compare_data_result)

                logging.info(f"result {index} : {compare_data_result}")
                
            except Exception as tile_error:
                logging.error(f"Error processing tile at index {index}: {tile_error}")

        return test_results

    except Exception as e:
        logging.error(f"Error during tile traversal and data extraction: {e}")


