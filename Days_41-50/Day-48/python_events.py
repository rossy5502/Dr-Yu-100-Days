from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = ("https://www.python.org/")
#to keep the webpage open
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)
driver = webdriver.Edge( options=edge_options)
#now working with the url
driver.get(url=url)
#now searching for time and event elements in upcoming events section

date=driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
event=driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# Debug: print all found elements
events={}
for i in range(len(date)):
    events[i] = {date[i].text: event[i].text}
print("Initial dict:", events)




driver.quit()