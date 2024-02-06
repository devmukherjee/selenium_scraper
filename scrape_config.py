"""
This is the config file used to save global config options.
This is a single point of control for all global configuration variables.
"""

DEBUG= True
from datetime import date
import os
"""Website configuration:"""

# master url is the first website to open when you start scraping.
master_url= "https://www.vistaprint.com/"

# Define the number of seconds to wait for an element to load
Web_Timeout= 30

""" Business Configuration"""
competitor= "VISTA"
scrape_date= date.today()
region= "US"

"""FILE PATHS"""
#Logging file
log_path= os.path.join(".","Log.txt")

#Input file
products_to_scrape_file_path= os.path.join(".","data","Products_to_scrape.xlsx")

#Output file
output_data_file_path= os.path.join(".","data","Output_data.csv")