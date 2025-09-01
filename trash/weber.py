# Importing Selenium libraries
import time
import klembord
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# State the Webdriver options
options = webdriver.ChromeOptions()

options.add_argument('--headless')


ser = Service(".\chromedriver.exe")

# Initiate the Chromedriver by passing options as argument
driver = webdriver.Chrome(service=ser, options=options)

# Obtain the web page
driver.get("https://spacy.io/usage/spacy-101")
start = [driver.title,]
ele = driver.find_elements(By.TAG_NAME, 'a')
def cont(driver):
    x = driver.save_screenshot('ss.png')
    #driver.send_keys(Keys.PAGE_DOWN)

    return x

def conn(driver):
    element = driver.find_element("xpath", "/html/body/div")
    x = element.get_attribute("innerHTML")


    klembord.set_with_rich_text(element.text, x)
    return x
print(driver.title)
cont(driver)
print(conn(driver))
