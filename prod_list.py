"""
This file contains utilities to read data from csv and preprocessing of Data

"""


import pandas as pd
import os 
import re

from scrape_config import DEBUG

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

def to_list(s1,delimiter=","):
    s= re.sub(r',\s*',",",s1)
    return s.split(delimiter)

def get_products_df(file_path):
    # root= os.getcwd()
    
    prod_list_df= pd.read_excel(file_path,skiprows=2,usecols=[1,2,3],engine="openpyxl")
    if(DEBUG):
        print(prod_list_df.head())
    
    # print(prod_list_df.columns)
    prod_list_df["Quantites"]=prod_list_df["Quantites"].map(lambda x: to_list(clean_quantitys(x)))
    prod_list_df["Color"]=prod_list_df["Color"].map(lambda x: to_list(x))
    
    if(DEBUG):
        print(prod_list_df["Quantites"])
        print("Type of first element of first element in Quantities:", type(prod_list_df["Quantites"][0][0]))

        print(prod_list_df["Color"])
        print("Type of first element of first element in Color", type(prod_list_df["Color"][0][0]))
        print(prod_list_df.dtypes)

    return prod_list_df

if __name__=="__main__":
    from scrape_config import products_to_scrape_file_path
    get_products_df(products_to_scrape_file_path)
#clean_quantitys("1-5,1-5")
