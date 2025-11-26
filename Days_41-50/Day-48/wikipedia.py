from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = ("https://en.wikipedia.org/wiki/Main_Page")
#to keep the webpage open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge( options=edge_options)
#now working with the url
driver.get(url=url)
stats=driver.find_elements(By.CSS_SELECTOR, '#articlecount a')
stats[1].click()  # Click first a tag

driver.close()