from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from utils.locator_reader import read_locators


def click_property_title_and_close_tab(driver, tile):
    try:
        locators = read_locators()

        title_locator = tile.find_element(By.XPATH,locators.get("title"))
        title = title_locator.text
        print(f"Clicking on title: {title}")

        # Open the new tab by clicking the title
        title_locator.click()
        
        # Wait for the new tab to open
        time.sleep(2)  # Adjust time as needed for the tab to load
        
        # Get all the window handles (tabs)
        window_handles = driver.window_handles
        
        # Switch to the new tab (last tab opened)
        driver.switch_to.window(window_handles[-1])
        
        # Do nothing here (or just wait for now)
        time.sleep(2)  # Simulating some idle time in the new tab
        
        # Close the new tab
        driver.close()
        
        # Switch back to the original tab (the first tab)
        driver.switch_to.window(window_handles[0])
        print(f"Switched back to the original tab: {window_handles[0]}")
        
    except Exception as e:
        print(f"Error during title click and tab switch: {e}")



