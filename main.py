from faker import Faker
from config import config
from utils.driver_setup import setup_driver
from tests.traverse_property_tiles import get_random_property_tiles
from tests.scroll_for_tiles import traverse_random_tiles
import logging
from tests.reading_xpaths import read_xpaths


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_tests():
    try:
        fake = Faker()

        # Generate a random city name
        random_city = fake.country()

        # Construct the full base URL
        base_url = f"{config.base_url_prefix}{random_city.replace(' ', '-').lower()}/"
        print(base_url)

        # Set up the WebDriver
        driver = setup_driver()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(2)


        # Add your test steps here
        random_tiles = get_random_property_tiles(driver)
        traverse_random_tiles(driver,random_tiles)

        
        

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Ensure the driver quits properly
        driver.quit()
       

if __name__ == "__main__":
    run_tests()


    