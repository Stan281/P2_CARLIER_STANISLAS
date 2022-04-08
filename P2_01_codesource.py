from selenium import webdriver
from selenium.webdriver.common.by import By

website = ('https://books.toscrape.com/catalogue/soumission_998/index.html')
path ='chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)

website_title = driver.find_elements(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
titles=[]
for i in range(len(website_title)):
    title=website_title[i].text
    titles.append(title)
print(titles)

driver.quit()