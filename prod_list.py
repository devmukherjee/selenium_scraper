import pandas as pd
import os 
import re

def clean_quantitys(s):
    match= re.match(r"(\d)-(\d)",s)
    if(not match):
        if(s[-1]==","):
            return s[:-1]
        else:
            return s
    else:
        start= int(match.group(1))
        end= int(match.group(2))
        new_range= list(range(start,end+1))
        print(new_range)
        new_strings= map(str,new_range)
        sub_str= ",".join(new_strings)
        # print(sub_str)
        final_string= re.sub(r"\d-\d",sub_str,s)
        if(final_string[-1]==","):
            return final_string[:-1]
        # print(final_string)
        else:
            return final_string



def get_products_df():
    root= os.getcwd()
    file_path= os.path.join(root,"selenium_scraper","data","Products_to_scrape.xlsx")
    prod_list_df= pd.read_excel(file_path,skiprows=2,usecols=[1,2,3])
    print(prod_list_df.head())
    print(prod_list_df.columns)
    prod_list_df["Quantites"]=prod_list_df["Quantites"].map(lambda x: clean_quantitys(x))
    print(prod_list_df["Quantites"])
    return prod_list_df

#clean_quantitys("1-5,1-5")
get_products_df()