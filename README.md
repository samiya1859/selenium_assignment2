
# Selenium Property Data Matching Project

This project automates the verification of property details (title, price, type, rating, reviews) on a property listing website. It checks the consistency of these details across multiple views: the property tile, the map info window, and the detail page.

## Features
- Extracts property data from tiles, map popups, and detailed property pages.
- Compares extracted data and generates a report of the test results.
- Uses random dynamic URLs for location-based property searches.
- Handles dynamic locators stored in an external configuration file.
- Implements a modular design for scalability and ease of maintenance.
- Uses Faker for generating random location data.
- Logs test execution and errors for easier debugging.

## Project Structure
```
selenium_assignment2/
|-- config/
|   |-- config.py  # Configuration settings.
|-- utils/
|   |-- driver_setup.py  # WebDriver initialization.
|   |-- locator_reader.py  # Reads locators from configuration.
|   |-- generate_excel.py  # Generates test reports in Excel format.
|-- tests/
|   |-- scroll_for_tiles.py  # Scrolls through property tiles.
|   |-- traverse_property_tiles.py  # Handles property data extraction.
|   |-- detail_page_data.py  # Extracts details from the property detail page.
|   |-- reading_xpaths.py  # Reads locators for dynamic elements.
|-- main.py  # Entry point for running the project.
|-- requirements.txt  # Dependencies.
|-- README.md  # Project documentation.
```

## Prerequisites
- Python 3.x
- Google Chrome
- Chromedriver compatible with your Chrome version

### Installing Chromedriver

1. Check your Chrome version by navigating to `chrome://settings/help`.
2. Download the matching Chromedriver from the official site: https://sites.google.com/chromium.org/driver/
3. Extract the downloaded archive.
4. Add the Chromedriver executable to your system PATH or specify the full path in `driver_setup.py`.

#### On Linux:
```bash
wget https://chromedriver.storage.googleapis.com/<version>/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
```

#### On Windows:
1. Extract `chromedriver_win32.zip`.
2. Place `chromedriver.exe` in a folder (e.g., `C:\chromedriver\`).
3. Add this folder to your system's PATH variable or update the path in the `setup_driver()` function.

## Setting Up
1. Clone the repository:
   ```
   git clone https://github.com/samiya1859/selenium_assignment2.git
   cd selenium_assignment2
   ```

2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate   # On Windows
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Project
To execute the tests and generate a report:
```bash
python main.py
```

The script will dynamically generate a location-based URL, traverse property data, and save the results in an Excel report.

## Configuration
- **config/config.py** contains the base URL prefix and other constants used for constructing dynamic URLs.
- **utils/locator_reader.py** reads locators from an external file for flexibility in locator management.

## Dynamic URL Checking
The project uses a loop to continuously check page layouts until a valid one is found. The process involves:
- Generating a random city name using `Faker`.
- Constructing a URL: `https://www.petfriendly.io/all/<random-city>/`.
- Checking the `window.ScriptData.pageLayout` value using JavaScript:
  - If layout is `"Error"`, a new URL is generated.
  - If layout is `"category"`, the tests proceed.

Example implementation in `check_page_layout.py`:
```python
page_layout = driver.execute_script("return window.ScriptData.pageLayout")
```

## Logging and Error Handling
- Logging is configured using Python’s `logging` module.
- Errors and retries are logged for better traceability.

Example logging configuration:
```python
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

## Test Flow
1. **Dynamic URL Generation**: A random city is selected, and a URL is constructed.
2. **URL Layout Check**: Loop until a valid layout is found.
3. **Data Extraction**: Property details are extracted from tiles and detail pages.
4. **Validation**: Consistency checks are performed between tiles, map info, and details pages.

## Generating Test Reports
Test results are saved in an Excel file:
- **utils/generate_excel.py** handles Excel report creation.
- The output includes test case results with status and comments.


## Test Data Report
The `generate_excel.py` script creates an Excel file summarizing the test results:
- `Key`: Unique identifier for each test.
- `URL`: Tested location-based URL.
- `Page`: Category page.
- `Test Case`: Data matching comparison.
- `Passed`: Boolean result.
- `Comments`: Detailed comparison outcomes.

## Future Enhancements
- Additional browser support.
- Expanded property data fields for verification.
- Parallel testing for improved performance.

This README provides comprehensive guidance for setting up, running, and understanding the project workflow. For any additional queries or issues, feel free to contact the project maintain




