from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd

path = Service('chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=path)

website_url = ('https://books.toscrape.com/catalogue/soumission_998/index.html')
driver.get(website_url)

product_page_url = driver.current_url
#print(product_page_url)
universal_product_code = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[1]/td')
title = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
price_including_tax = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[4]/td')
price_excluding_tax = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[3]/td')
number_available = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[6]/td')
product_description = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/p')
category = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[2]/td')
review_rating = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/table/tbody/tr[7]/td')
image_url = driver.find_elements(By.XPATH, '//*[@id="product_gallery"]/div/div/div/img')
for ele in image_url:
  x=ele.get_attribute('src')
#print(x)

book=[]
for i in range(len(title)):
    book_info={}
    book_info['product_page_url']=product_page_url[i]
    book_info['universal_product_code']=universal_product_code[i].text
    book_info['title']=title[i].text
    book_info['price_including_tax']=price_including_tax[i].text
    book_info['price_excluding_tax']=price_excluding_tax[i].text
    book_info['number_available']=number_available[i].text
    book_info['product_description']=product_description[i].text
    book_info['category']=category[i].text
    book_info['review_rating']=review_rating[i].text
    book_info['image_url']=x[i]
    book.append(book_info)
#print(book)

driver.quit()

#CREATION BDD ET EXTRACTION BDD VERS CSV
df=pd.DataFrame(book,columns=['product_page_url','universal_product_code','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url'])
df.to_csv('extractbook.csv')