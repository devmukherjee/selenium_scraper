from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
from logging import Logger

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach",True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--incognito")

driver= webdriver.Chrome(service= Service(ChromeDriverManager().install()), options= options)
master_url= "https://www.vistaprint.com/"
logger= Logger("Newlogger")

actions = ActionChains(driver)
try:

    driver.get(master_url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    wait = WebDriverWait(driver, 30)
    
except Exception as e:
    msg= f"ERROR: Error connecting to the url: {master_url} \n please retry: \n Exception: {e}"
    # logger.error(msg= msg)
    print(msg)

# def scrape_product(driver,name,quantity,color):
#     pass
#     driver.
    
search_bar= driver.find_element("xpath",'//input[contains(@class,"site-header-search")]')
# from prod_list import get_products_df
# # print(search_bar.get_attribute("placeholder"))
# products= get_products_df()
# first_prod= products["Product Name"][0]
# print(first_prod)
first_prod= "Aluminum Water Bottle with Carabiner – 26 oz."
search_bar.send_keys(first_prod)
import time

time.sleep(10)
located= wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"search-flyout")]//div[contains(@class,"search-results-analytics-section")]')))
# actions.send_keys(Keys.ENTER)
# actions.perform()
if(located):
    product_link= wait.until(EC.visibility_of_element_located((By.XPATH,'//div[contains(@class,"search-results-analytics-section")][@data-search-analytics-section-name="PRODUCTS"]//div[contains(@class,"search-result-analytics-result")]/a[.//span[text()[contains(.,"Aluminum Water Bottle with Carabiner – 26 oz.")]]]')))
    # driver.find_element("xpath",'//div[contains(@class,"search-flyout")]')
                                #   //div[contains(@class,"search-result-analytics-section")][@section-name="PRODUCTS"]//div[contains(@class,"search-result-analytics-result")]//a[.//span[text()[contains(.,"Aluminum Water Bottle with Carabiner – 26 oz.")]]]')

# product_link= driver.find_element("xpath",'//div[contains(@class,"search-result-analytics-section")][@data-search-analytics-section-name="Products"]')
# [@section-name="PRODUCTS"]//div[contains(@class,"search-result-analytics-result")]//a[.//span[text()[contains(.,"Aluminum Water Bottle with Carabiner – 26 oz.")]]]')

print(product_link)

print("This line is being executed: \n", product_link.get_attribute("innerHTML"))

product_link.click()
