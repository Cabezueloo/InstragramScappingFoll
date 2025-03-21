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
USERNANE = "recreatiupolinya"

FRAME_FOLLOWERS_FOLLOWING = "'xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6'"
NAME_FOLLOWERS_FOLLOGIN = "'_ap3a _aaco _aacw _aacx _aad7 _aade'"

FRAME_VIWED_HISTORY = "'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 xw2csxc x1odjw0f x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'"
NAME_VIWED_HISTORY = "'x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj'"

SPAN_TOTAL_FOLLOWERS = "'html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs'"


class SeleniumInstagram:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.account = USERNANE
        self.url = BASE_URL+self.account+"/"
        self.followers = list()
        self.views      = set(())
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
        # Locate the element using class name and get the title attribute
        element = self.driver.find_elements(By.XPATH, "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xl565be xo1l8bm x1roi4f4 x2b8uid x10wh9bi x1wdrske x8viiok x18hxmgj']")[2]  # Adjust class if needed

        totalFollowers = int(element.text.split(" ")[0])
        print(f"Total followers -> {totalFollowers}")

        if followers:
            search = FOLLOWERS
            f= open("followers/followers.txt","w")
        else:
            search = FOLLOWING
            f= open("following/following.txt","w")
        

        #Open Followers 
        elementFollowersToClick = self.driver.find_element(By.XPATH, f"//a[@href='/{USERNANE}{search}']")
        elementFollowersToClick.click()
        
        frame  = self.driver.find_element(By.XPATH,f"//div[@class={FRAME_FOLLOWERS_FOLLOWING}]")
        scroll_origin = ScrollOrigin.from_element(frame)
        names =  set({})
        salto = 75

        while len(names)<totalFollowers:
            
            elements = self.driver.find_elements(By.XPATH, f"//*[@class={NAME_FOLLOWERS_FOLLOGIN}]")
                
            for element in elements:
                names.add(element.text)
      
            if len(names)>150:
                salto = 125
            if len(names)>200:
                salto = 175
            elif (len(names)>300):
                salto = 220
            elif (len(names)>400):
                salto = 275
            elif (len(names)>500):
                salto = 350 
            ActionChains(self.driver)\
            .scroll_from_origin(scroll_origin,0,int(salto))\
            .perform()
            
            print(f"Tamagno -> {len(names)}" )
                
        print("SALIO")
        #Fuera while true

        f.write(USERNANE+"\n")
        for name in names:
            self.followers.append(name)
            f.write(f"{name}\n")

       
             
    def seeVisitedHistory(self):
        
        
        self.driver.get("https://www.instagram.com/stories/archive/18299908186225234/?initial_media_id=3572457676619689748")

        element = self.driver.find_element(By.XPATH, "//span[@class='xfungia x1yxbuor x19qstwj x1yrs1ss']")
        element.click()
        time.sleep(4)

        frame  = self.driver.find_element(By.XPATH,f"//div[@class={FRAME_VIWED_HISTORY}]")
        scroll_origin = ScrollOrigin.from_element(frame)
        lastElementName=""
        tryAagain = True
    

        while True:
            
            names = self.driver.find_elements(By.XPATH, f"//span[@class={NAME_VIWED_HISTORY}]")
            
            for name in names:
                #print(name.text)
                self.views.add(name.text)
           # print(names[-1].rect)
            #print(names[-1].rect['y'])
           # print(print(names[-1].text))

            ActionChains(self.driver)\
            .scroll_from_origin(scroll_origin,0,int(names[-1].rect['y']))\
            .perform()

            
            time.sleep(0.5)
            
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
        names = self.driver.find_elements(By.XPATH, f"//span[@class={NAME_VIWED_HISTORY}]")

        for name in names:
            self.views.add(name.text)
