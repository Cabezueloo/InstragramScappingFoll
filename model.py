from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
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
    
    
    def modelStartAnalyseFollowers(self,followers=True):
        
        search = ""
        if followers:
            search = FOLLOWERS
        else:
            search = FOLLOWING
        
        #Open Followers 
        elementFollowersToClick = self.driver.find_element(By.XPATH, f"//a[@href='/{USERNANE}{search}']")
        elementFollowersToClick.click()
        actualName = ""
        
        frame  = self.driver.find_element(By.XPATH,"//div[@class='xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6']")
        scroll_origin = ScrollOrigin.from_element(frame)
        last_y = -1
        tryAagain = True

        lastElementName = ""
        
        while True:
            
            names = self.driver.find_elements(By.XPATH, "//*[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']")
            

           # print(names[-1].rect)
            #print(names[-1].rect['y'])
           # print(print(names[-1].text))

            ActionChains(self.driver)\
            .scroll_from_origin(scroll_origin,0,int(names[-1].rect['y']))\
            .perform()
            
            
            if lastElementName != names[-1].text:
                lastElementName = names[-1].text
                tryAagain = True
            else:
                if tryAagain:
                    time.sleep(1) 
                    tryAagain = False       
                    continue
                break

        #Fuera while true
        names = self.driver.find_elements(By.XPATH, "//*[@class='_ap3a _aaco _aacw _aacx _aad7 _aade']")

        for name in names:
            self.followers.append(name.text)

        #print(self.followers)
       # print(f"Tamagno -> {len(self.followers)}")
             
        
        
       



        
        



