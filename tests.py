import unittest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Import time for potential delays
import os
from scrape_config import master_url, Web_Timeout, scrape_date, region, competitor, products_to_scrape_file_path, output_data_file_path, DEBUG  # Import config variables
from scraper_vista import scrape_all_configurations_product, clean_output_df  # Import your scraping functions (replace your_scraping_script with the actual name of your script)
from prod_list import get_products_df # Assuming prod_list.py is in the same directory

# Mock log_error function for testing
def mock_log_error(message):
    print(f"ERROR (TEST): {message}")  # Print errors during testing
    # You could also store these in a list for later assertion if needed

class VistaPrintScraperTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)  # Keep browser open after test
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, Web_Timeout)
        self.driver.get(master_url)  # Open the main URL before each test
        self.driver.maximize_window()
        self.data_dicts_list = []  # Initialize data_dicts_list here
        global log_error # Use the mock
        log_error = mock_log_error

    def tearDown(self):
      if self.driver:
        self.driver.quit()  # Close the browser after each test
        try:
            os.remove(output_data_file_path)  # Clean up the output file after test
        except FileNotFoundError:
            pass # If the file doesnt exist

    def test_initialization_navigation(self):
        self.assertIn("VistaPrint", self.driver.title)  # Check if the website title is correct

    def test_product_search_valid(self):
        search_name = "Aluminum Water Bottle with Carabiner – 26 oz." # Example, change as needed
        scrape_all_configurations_product(colors=['Red'], quantitites=[2], search_name=search_name)
        self.assertGreater(len(self.data_dicts_list), 0)  # check if data was scraped

    def test_product_search_invalid(self):
        search_name = "NonExistentProduct"
        scrape_all_configurations_product(colors=['Red'], quantitites=[2], search_name=search_name)
        self.assertEqual(len(self.data_dicts_list), 0)  # No data should be collected

    def test_data_extraction_pattern1(self):
        # Assuming "Aluminum Water Bottle" is Pattern 1
        search_name = "Aluminum Water Bottle with Carabiner – 26 oz."
        scrape_all_configurations_product(colors=['Red'], quantitites=[2], search_name=search_name)
        self.assertGreater(len(self.data_dicts_list), 0)
        data = self.data_dicts_list[0]
        self.assertIn("Aluminum Water Bottle", data["Product_Name"])
        self.assertIsNotNone(data["List_Price"]) # Check if price was scraped

    def test_data_extraction_pattern2(self):
        # Add a product name that you know uses pattern 2
        # Example: search_name = "Product Name Pattern 2"
        # scrape_all_configurations_product(colors=['Red'], quantitites=[2], search_name=search_name)
        # self.assertGreater(len(self.data_dicts_list), 0)
        # data = self.data_dicts_list[0]
        # self.assertIn("Product Name Pattern 2", data["Product_Name"])
        # self.assertIsNotNone(data["List_Price"])
        pass # If you do not have a pattern 2 product for testing

    def test_data_extraction_unavailable_color(self):
        search_name = "Aluminum Water Bottle with Carabiner – 26 oz."
        scrape_all_configurations_product(colors=['NonExistentColor'], quantitites=[2], search_name=search_name)
        self.assertGreater(len(self.data_dicts_list), 0) # Check if data was scraped

    def test_data_extraction_unavailable_quantity(self):
         search_name = "Aluminum Water Bottle with Carabiner – 26 oz."
         scrape_all_configurations_product(colors=['Red'], quantitites=['NonExistentQuantity'], search_name=search_name)
         self.assertGreater(len(self.data_dicts_list), 0) # Check if data was scraped

    def test_data_processing_duplicate_removal(self):
        # Add duplicate data to data_dicts_list (for testing purposes)
        self.data_dicts_list = [{"Product_Name": "Test", "Color": "Red", "Quantity": 2}] * 2
        df = pd.DataFrame(self.data_dicts_list)
        cleaned_df = clean_output_df(df)
        self.assertEqual(len(cleaned_df), 1)  # Ensure duplicates are removed

    def test_data_output_csv(self):
        self.data_dicts_list = [{"Product_Name": "Test", "Color": "Red", "Quantity": 2}]
        df = pd.DataFrame(self.data_dicts_list)
        df.to_csv(output_data_file_path, index=False)  # Write to the test output path
        self.assertTrue(os.path.exists(output_data_file_path))  # Check if file exists
        read_df = pd.read_csv(output_data_file_path)
        self.assertEqual(len(read_df), 1)

    def test_edge_case_empty_input(self):
        # Create an empty input file for testing
        empty_df = pd.DataFrame(columns=["Product Name", "Color", "Quantites"])
        empty_df.to_csv(products_to_scrape_file_path, index=False)
        main() # Call main, so it reads the file
        self.assertTrue(os.path.exists(output_data_file_path))
        read_df = pd.read_csv(output_data_file_path)
        self.assertEqual(len(read_df), 0) # Expect empty file


    def test_edge_case_no_matching_product(self):
        search_name = "NonExistentProduct"
        scrape_all_configurations_product(colors=['Red'], quantitites=[2], search_name=search_name)
        self.assertEqual(len(self.data_dicts_list), 0)  # No data should be collected

    def test_main_function(self):
        # Create a test input CSV
        test_data = {'Product Name': ['Test Product'], 'Color': [['Red']], 'Quantites': [[2]]}
        test_df = pd.DataFrame(test_data)
        test_df.to_csv(products_to_scrape_file_path, index=False)

        # Run the main function
        from scraper_vista import main  # Import the main function
        main()

        # Check if the output CSV was created and has data
        self.assertTrue(os.path.exists(output_data_file_path))
        output_df = pd.read_csv(output_data_file_path)
        self.assertGreater(len(output_df), 0)

if __name__ == "__main__":
    from scraper_vista import main # Import main here to avoid circular imports
    unittest.main()