from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://www.jumia.com.ng/groceries/")
time.sleep (5)

soup=BeautifulSoup(driver.page_source, "lxml")
product=soup.find_all("article",class_="prd")

data=[]

for p in product:
     name= p.find("div", class_="name")
     price= p.find("div",class_="prc")
     discount= p.find("div", class_= "bdg _dsct _sm")
     rating= p.find("div", class_= "in")

     data.append ( {"names": name. text.strip() if name else "missing" , 
               "prices": price. text.strip() if price else "missing" , 
              "discounts":discount.text.strip() if discount else "missing" ,
             "ratings": rating.text.strip() if rating else "missing "})

driver.quit()

df=pd.DataFrame(data)
print(df.head(10))
print(len(df))

print(df.head(50))

df.to_csv("jumia_products", index=False, encoding="utf-8=sig" )
print("data saved to jumia_products.csv")

#df= pd.read_csv("jumia_products.csv")
#print(df.head(10))

import os
print(os.getcwd())