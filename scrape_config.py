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
