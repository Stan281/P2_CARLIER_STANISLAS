from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

path = Service('chromedriver_linux64/chromedriver')
driver = webdriver.Chrome(service=path)
website = ('https://books.toscrape.com/catalogue/soumission_998/index.html')
driver.get(website)

website_title = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
website_desc = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/p')

book=[]
for i in range(len(website_title)):
    book_info={}
    book_info['title']=website_title[i].text
    book_info['description']=website_desc[i].text
    book.append(book_info)
print(book)

'''website_title = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')

titles=[]
for i in range(len(website_title)):
    title=website_title[i].text
    titles.append(title)
print(titles)'''

driver.quit()