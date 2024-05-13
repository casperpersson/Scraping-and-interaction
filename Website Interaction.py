from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("https://billigtshirt.dk/")

search = driver.find_element(By.CSS_SELECTOR, "#clerk-search-filters")
search.send_keys("sweatshirt")
search.send_keys(Keys.ENTER)