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

from scrape_config import DEBUG

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
    wait = WebDriverWait(driver, 10)
    
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


def scrape_one_product_configuration(product_name="name",product_category="Box",color="Red",quantity=2,region="US",decoration_tech="Digital Inkjet"):
    """
    SCRAPING PRODUCT CONFIGURATIONS
    """
    try:
    #clcicking the color radio button
        color_control_label= wait.until(EC.visibility_of_element_located((By.XPATH, f'//div[contains(@class,"swan-selection-set")][@role="radiogroup"]//label[.//span[contains(@class,"swan-color-swatch-accessible-label")][text()[contains(.,"{color}")]]]')))
    except Exception as e:
        print("Color Not Available for the following product:\n Product Name: {product_name}")
        color_control_label= wait.until(EC.visibility_of_all_elements_located((By.XPATH, f'//div[contains(@class,"swan-selection-set")][@role="radiogroup"]//label[.//span[contains(@class,"swan-color-swatch-accessible-label")]]]')))[0]
    # print("Auto Generated ID for radio button is: ",color_control_label.get_attribute("for"))
    # radio_id= color_control_label.get_attribute("for")
    # color_radio_button= driver.find_element("xpath",f'//div//input[@type="radio"][@id="{radio_id}"]')
    # print("Auto Generated ID for radio button is: ",color_radio_button.get_attribute("id"))
    # actions.move_to_element(color_radio_button).perform()
    try:
        actions.move_to_element(color_control_label)
        actions.double_click(on_element= color_control_label)
        actions.perform()
    except Exception as e:
        print("Color button Not clickable, Aborting data scraping for current configuration \n {e}")
        return
        
    #getting the quantity button
    try:
        quantity_button= wait.until(EC.visibility_of_element_located((By.XPATH,'//div//span[@role="button"][contains(@class,"swan-legacy-listbox-button-with-label")]')))
        quantity_button.click()
    except Exception as e:
        print("Quantity button Not clickable, Aborting data scraping for current configuration \n {e}")
        return

    #Mind to check for quantity 250+ becuase there is no price given.
    try:
        desired_quantity_item= wait.until(EC.presence_of_element_located((By.XPATH,f'//ul[@id="listbox--builder-quantity-dropdown"]//li[@data-value="{quantity}"]')))
        desired_quantity_item.click()
    except Exception as e:
        print("Desired Quantity button Not clickable, Aborting data scraping for current configuration \n {e}")
        return
    
    if(quantity=="250+"):
        list_price= 'Get_quote'
    else:
        try:
            list_price= wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class,"price-block")]//span[contains(@class,"swan-list-price")]'))).text
        except Exception as e:
          print("List price button Not Visible, Aborting data scraping for current configuration \n {e}")
          return  
    print("List price for quantity:",quantity,"is",list_price)

    product_data={}
    product_data["Product_Name"]= product_name
    product_data["Product_category"]= product_category
    product_data["Color"]= color
    product_data["Quantity"]= quantity
    product_data["List_Price"]= list_price
    product_data["url"]= driver.current_url
    return product_data
    
def scrape_all_configurations_product(colors,quantitites,search_name="Aluminum Water Bottle with Carabiner – 26 oz.",search_bar= search_bar):
    """
    Navigatting to the product
    """
    first_prod= "Aluminum Water Bottle with Carabiner – 26 oz."
    search_bar.send_keys(search_name)
    import time

    # time.sleep(10)
    located= wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class,"search-flyout")]//div[contains(@class,"search-results-analytics-section")]')))
    # actions.send_keys(Keys.ENTER)
    # actions.perform()
    if(located):
        # product_link= wait.until(EC.visibility_of_element_located((By.XPATH,'//div[contains(@class,"search-flyout")]//div[contains(@class,"search-results-analytics-section")][@data-search-analytics-section-name="PRODUCTS"]//div[contains(@class,"search-result-analytics-result")]/a[.//span[text()[contains(.,"Aluminum Water Bottle with Carabiner – 26 oz.")]]]')))
        product_link= wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//div[contains(@class,"search-flyout")]//div[contains(@class,"search-results-analytics-section")][@data-search-analytics-section-name="PRODUCTS"]//div[contains(@class,"search-result-analytics-result")]/a')))[0]
        # driver.find_element("xpath",'//div[contains(@class,"search-flyout")]')
                                    #   //div[contains(@class,"search-result-analytics-section")][@section-name="PRODUCTS"]//div[contains(@class,"search-result-analytics-result")]//a[.//span[text()[contains(.,"Aluminum Water Bottle with Carabiner – 26 oz.")]]]')

    # product_link= driver.find_element("xpath",'//div[contains(@class,"search-result-analytics-section")][@data-search-analytics-section-name="Products"]')
    # [@section-name="PRODUCTS"]//div[contains(@class,"search-result-analytics-result")]//a[.//span[text()[contains(.,"Aluminum Water Bottle with Carabiner – 26 oz.")]]]')

    print(product_link)
    product_href_wo_query= product_link.get_attribute("href").split("?")[0]

    print("This line is being executed: \n", product_link.get_attribute("innerHTML"))


    product_link.click()

    #check pageload
    located= wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class,"swan-selection-set")][@role="radiogroup"]')))

    if(located):
        
        try:
            product_name= driver.find_element("xpath",'//div//h1[contains(@class,"product-name")]').text
            print("Products name is: ",product_name)
        except Exception as e:
            print("Product Name not found \n Failed with error {e}, \n Using url to find product name")
            product_name = product_href_wo_query.split("/")[-1]

        # finding the li tag containing the link of product in the category display span element above the
        #product image
        
        try:
            #Use wait function to ensure the section with category links is loaded.
            #get a list of all a tags one for each category.
            pli= wait.until(EC.visibility_of_all_elements_located(("xpath",f'//section[.//li//a[text()[contains(.,"{product_name}")]]]//li//a')))
            product_category= pli[-2].text
            # product_category= pli.find_element("xpath","preceding-sibling::*[1]").find_element()
            # .find_element("xpath",'//a').text 
            # print('New Product category :', product_category.get_attribute("innerHTML"))
            print('New Product category :', product_category)
        except Exception as e:
            print(f"Category links did not load \n Failed with the follwoing error: {e}/n Calculating category based on url")
            
            product_category= product_href_wo_query.split("/")[-2]
                # print('Product category :', product_category)
                # product_category="Category Not Found"
            
        try:
            product_decoration_item= wait.until(EC.visibility_of_element_located((By.XPATH,'//div[@id= "Overview"][@role="tabpanel"]//p[.//strong[text()[contains(.,"Decoration")]]]')))
            product_decoration_tech= product_decoration_item.text
            print("Decoration Technology is: ", product_decoration_tech )
            time.sleep(2)
        except Exception as e:
            print(f"Decoration Technology Not Found \n Failed with error: {e}")
            product_decoration_tech= "Not Found"
        
        
        print("Navigation and image now visible")

        for color in colors:
            for quantity in quantitites:
                product_data= scrape_one_product_configuration(product_name=product_name,product_category=product_category,color= color,quantity=quantity,region="US",decoration_tech=product_decoration_tech)
                print("Data for one configuration is:", product_data)

    else:
        print("Product Page did not load details are : \n Product Search Name:{search_name} ")    

#scrape_all_configurations_product(colors=['Red','Blue'],quantitites=[2,3])    # radio_button.click()

from prod_list import get_products_df
if(DEBUG):
    print(get_products_df().head())

products_to_scrape_df= get_products_df()

for index,row in products_to_scrape_df.iterrows():
    scrape_all_configurations_product(colors= row["Color"],quantitites=row["Quantites"],search_name= row["Product Name"],search_bar= search_bar)


