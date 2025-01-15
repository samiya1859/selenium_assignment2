from selenium.webdriver.common.by import By
import time
from utils.locator_reader import read_locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_map_icon(driver, tile):

    locators = read_locators()

    try:
        map_icon_locator = locators.get("map_icon")
        if not map_icon_locator:
            raise ValueError("Map icon locator not found in locators file.")
        
        print(f"Locator for map icon: {map_icon_locator}")
        
        map_icon = tile.find_element(By.XPATH, map_icon_locator)
        
        # Wait for the element to be clickable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(map_icon))
        
        # Scroll into view if necessary
        ActionChains(driver).move_to_element(map_icon).perform()
        
        # Click the map icon
        map_icon.click()
        
        # Log successful click
        print("Map icon clicked.")
        time.sleep(2)
        
    except Exception as e:
        print(f"Failed to click map icon: {e}")