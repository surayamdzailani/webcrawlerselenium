from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(option)
driver.get("https://www.amazon.sg")
driver.maximize_window()

search_box = driver.find_element(By.XPATH,'//input[@id="twotabsearchtextbox"]')
search_box.clear()
search_box.send_keys("manga")

click_search_button = driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]')
click_search_button.click()

filter_data = driver.find_element(By.XPATH, "//span[text()='Last 30 Days']")
filter_data.click()

filter_rating = driver.find_element(By.XPATH, "//span[text()='& Up']")
filter_rating.click()



#create empty list to store all our info that we want to scrape
manga_name = []
manga_price = []
manga_reviews = []

#scrape info product 
#all items
#name
names = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
for name in names:
	manga_name.append(name.text)
#price
prices = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")
for price in prices:
	manga_price.append(price.text)
#reviews
reviews = driver.find_elements(By.XPATH, "//span[@class = 'a-size-base s-underline-text']")
for review in reviews:
	manga_reviews.append(review.text)


print('name=====>', len(manga_name))
print('price=====>', len(manga_price))
print('review=====>', len(manga_reviews))

#import into cvs

import pandas as pd 
df = pd.DataFrame(zip(manga_name,manga_price, manga_reviews), columns=['manga_name', 'manga_price', 'manga_reviews'])
df.to_excel(r"C:\Users\yunz\Documents\web craweler selenium_shoppe product\manga_data.xlsx", index=False)