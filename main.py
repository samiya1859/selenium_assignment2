from faker import Faker
import time
import logging
from utils.driver_setup import setup_driver
from config import config
from utils.generate_excel import generate_excel
from tests.traverse_property_tiles import get_random_property_tiles
from tests.scroll_for_tiles import traverse_random_tiles

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_page_layout(driver, fake):
    """
    Check the page layout by evaluating the JavaScript variable 'window.ScriptData.pageLayout'.
    If it's 'Error', retry with a new URL; if 'category', proceed with functionality.
    """
    try:
        # Get the page layout from JavaScript
        page_layout = driver.execute_script("return window.ScriptData.pageLayout")
        logging.info(f"Page Layout: {page_layout}")

        if page_layout.lower() == "error":
            logging.error("Page Layout is 'Error'. Generating a new URL to retry...")
            # Generate a new random city name and URL for retry
            random_city = fake.country()
            new_url = f"{config.base_url_prefix}{random_city.replace(' ', '-').lower()}/"
            driver.get(new_url)  # Navigate to the new URL
            driver.implicitly_wait(2)
            return False  # Indicates we should retry with a new URL
        elif page_layout.lower() == "category":
            return True  # Indicates valid layout found, break loop and continue
        else:
            logging.warning(f"Unexpected page layout: {page_layout}")
            return False  # Handle unexpected layouts and retry
    except Exception as e:
        logging.error(f"Error retrieving page layout: {e}")
        return False  # Handle the error scenario and retry

def run_tests():
    try:
        fake = Faker()
        
        # Initial base URL generation with a random city
        random_city = fake.country()
        base_url = f"{config.base_url_prefix}{random_city.replace(' ', '-').lower()}/"
        logging.info(f"Checking URL: {base_url}")

        
        # Set up the WebDriver
        driver = setup_driver()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)

        # Loop until valid page layout is found
        while True:
            # Check page layout
            if check_page_layout(driver, fake):
                break  # Exit the loop if the layout is 'category'
            time.sleep(2)  # Wait before retrying if the layout is 'Error'

        # Proceed with the test steps once valid layout is found
        random_tiles = get_random_property_tiles(driver)
        test_results = traverse_random_tiles(driver, random_tiles)

        # Generate the results into an Excel file
        generate_excel(key="petfriendly.io", page="category", url=base_url, test_results=test_results)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Ensure the driver quits properly
        driver.quit()

if __name__ == "__main__":
    run_tests()
