from utils.locator_reader import read_locators

def read_xpaths(driver):
    """
    Reads all XPaths from the Excel file and prints them for debugging.
    
    Args:
        driver (webdriver): The Selenium WebDriver instance.
    """
    # Read locators from the Excel file
    locators = read_locators()
    
    # print("Reading all XPaths from Excel:")

    # # Print all locators
    # for element, xpath_value in locators.items():
    #     print(f"Element: {element}, XPath: {xpath_value}")

    # Print individual elements
    tiles_container_xpath = locators.get("tiles_container")
    property_tile_xpath = locators.get("property_tile")

    print(f"\nIndividual elements:")
    print(f"tiles_container XPath: {tiles_container_xpath}")
    print(f"property_tile XPath: {property_tile_xpath}")

