from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pickle

BASE_URL : str = "https://www.instagram.com/"
FOLLOWERS : str = "/followers/"
FOLLOWING : str = "/following/"
ROUTE_COOKIES = "cookie_login/"
USERNANE = "angeel.bjj"

class SeleniumInstagram:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.account = USERNANE
        self.url = BASE_URL+self.account+"/"
        self.followers = list()

        self.driver.implicitly_wait(3.0) # Wait 3 seconds into get a element
        self.login()

    def login(self):
    
        self.driver.get(self.url)

        for x in range(1,9):
            
            cookies = pickle.load(open(f"{ROUTE_COOKIES}cookie{x}.pkl","rb"))
                        
            self.driver.add_cookie(cookies)
        
        self.driver.refresh()
    
    
    def modelStartAnalyseFollowers(self):
        
        #Open Followers 
        elementFollowersToClick = self.driver.find_element(By.XPATH, f"//a[@href='/{USERNANE}/followers/']")
        elementFollowersToClick.click()
        actualName = ""

        lastElementName = ""
        
        while True:
            names = self.driver.find_elements(By.XPATH, "//*[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']")

            for name in names:
                self.followers.append(name.text)

            #Get to end            if self.followers[-1] == lastElementName:
                break

            lastElementName = self.followers[-1]
            
            
            ActionChains(self.driver)\
            .move_to_element(names[-1])\
            .perform()

            print(self.followers)
        
        
       



        
        



