"""
This is the config file used to save global config options.
This is a single point of control for all global configuration variables.
"""

DEBUG= True
from datetime import date
import os
# Website configuration:
master_url= "https://www.vistaprint.com/"
Web_Timeout= 30
competitor= "VISTA"
scrape_date= date.today()
region= "US"
log_path= os.path.join(".","Log.txt") 

products_to_scrape_file_path= os.path.join(".","data","Products_to_scrape.xlsx")
output_data_file_path= os.path.join(".","data","Output_data.csv")