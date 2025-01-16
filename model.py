from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SeleniumInstagram:
    
    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3.0) # Wait 3 seconds into get a element
        self.url = url
        self.driver.get(url=self.url) # Load a the page to the person get follw
