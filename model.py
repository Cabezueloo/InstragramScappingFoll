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
USERNANE = "maariacbv"

FRAME_FOLLOWERS_FOLLOWING = "'xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6'"
NAME_FOLLOWERS_FOLLOGIN = "'_ap3a _aaco _aacw _aacx _aad7 _aade'"

FRAME_VIWED_HISTORY = "'x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 xw2csxc x1odjw0f x1iyjqo2 x2lwn1j xeuugli xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1'"
NAME_VIWED_HISTORY = "'x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj'"

SPAN_TOTAL_FOLLOWERS_OR_FOLLOWING = "'x1lliihq x1plvlek xryxfnj x1n2onr6 x1ji0vk5 x18bv5gf x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xl565be xo1l8bm x1roi4f4 x2b8uid x10wh9bi x1wdrske x8viiok x18hxmgj'"

ROUTE_FILE_FOLLOWERS_OLDER = "followers/older_followers.txt"
ROUTE_FILE_FOLLOWERS_NEWEST = "followers/newest_followers.txt"

ROUTE_FILE_FOLLOWING_OLDER = "following/older_following.txt"
ROUTE_FILE_FOLLOWING_NEWEST = "following/newest_following.txt"


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
    
    
    """
    :param self:
    :param modeFollores: Boolean that activate search by followers or search by following
    :param first_scanner: Boolean that decide in that file we will save the log
    """

    def modelStart(self,modeFollowers:bool,first_scanner:bool):
        

        searchBy = ""
        
        # Locate the element box total (followers/following) using class name and get the title attribute
        element = self.driver.find_elements(By.XPATH, f"//span[@class={SPAN_TOTAL_FOLLOWERS_OR_FOLLOWING}]")[1 if modeFollowers else 2]  # Adjust class if needed

        total_followers_or_following = int(element.text.split(" ")[0].replace(",",""))
        print(f"Total followers -> {total_followers_or_following}")

        if modeFollowers:
            searchBy = FOLLOWERS
            file = open(f"{ROUTE_FILE_FOLLOWERS_OLDER}" if first_scanner else f"{ROUTE_FILE_FOLLOWERS_NEWEST}","w")
        else:
            searchBy = FOLLOWING
            file = open(f"{ROUTE_FILE_FOLLOWING_OLDER}" if first_scanner else f"{ROUTE_FILE_FOLLOWING_NEWEST}","w")
        
        

        #Open windows Follow* 
        elementFollowersToClick = self.driver.find_element(By.XPATH, f"//a[@href='/{USERNANE}{searchBy}']")
        elementFollowersToClick.click()
        
        frame  = self.driver.find_element(By.XPATH,f"//div[@class={FRAME_FOLLOWERS_FOLLOWING}]")
        scroll_origin = ScrollOrigin.from_element(frame)
        
        #Where we save the name
        names =  set({})
        
        salto = 50


        while len(names)+1<total_followers_or_following:
            
            elements = self.driver.find_elements(By.XPATH, f"//*[@class={NAME_FOLLOWERS_FOLLOGIN}]")
                
            for element in elements:
                names.add(element.text)
                  
            ActionChains(self.driver)\
            .scroll_from_origin(scroll_origin,0,int(salto))\
            .perform()
            
            salto+=3
            print(f"Tamagno -> {len(names)}" )
            print(f"Salto -> {salto}" )
                
        print("SALIO")
        #Fuera while true

        file.write(USERNANE+"\n")
        for name in names:
            #self.followers.append(name)
            file.write(f"{name}\n")

        if not first_scanner:
            
            file_old = open(f"{ROUTE_FILE_FOLLOWERS_OLDER}") if modeFollowers else open(f"{ROUTE_FILE_FOLLOWING_OLDER}","r")
            oldest_foll = []
            
            dejo = []
            nuevo =  []

            for line in file_old:
                oldest_foll.append(line.replace("\n",""))
            
            names_copy = names.copy()

            for newest in names_copy:
                if(oldest_foll.__contains__(newest)):
                    oldest_foll.remove(newest)
                    names.remove(newest)

            print(len(names))
            
            for resto in names:
                print(f"Nuevo -> {resto}")
            
            for resto in oldest_foll:
                print(f"Dejo de seguir -> {resto}")




            

        

       
             
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
