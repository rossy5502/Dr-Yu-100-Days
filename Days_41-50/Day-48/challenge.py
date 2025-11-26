from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = ("https://secure-retreat-92358.herokuapp.com/")
#to keep the webpage open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge( options=edge_options)
#now working with the url
driver.get(url=url)
#now searching for time and event elements in upcoming events section
first_name=driver.find_element(By.NAME, "fName")
first_name.send_keys("Siddharth")
last_name=driver.find_element(By.NAME, "lName")
last_name.send_keys("Raj")
email=driver.find_element(By.NAME, "email")
email.send_keys("siddharth.raj@gll.cl")
submit=driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
submit.click()
#driver.quit()
