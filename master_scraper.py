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

from scrape_config import DEBUG

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





