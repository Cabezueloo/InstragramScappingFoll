from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time
import pickle
from constants import *
import os

class SeleniumInstagram:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.account = USERNANE
        self.url = BASE_URL+self.account+"/"
        self.followers = list()
        self.views      = set(())
        self.driver.implicitly_wait(4.0) # Wait 3 seconds into get a element
        self.login()

    def login(self):
    
        self.driver.get(self.url)

        for x in range(1,9):
            
            cookies = pickle.load(open(f"{ROUTE_FILE_OUR_COOKIES}cookie{x}.pkl","rb"))
                        
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
        element = self.driver.find_elements(By.XPATH, f"//span[@class={WEB_SPAN_TOTAL_FOLLOWERS_OR_FOLLOWING}]")[1 if modeFollowers else 2]  # Adjust class if needed

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
        
        frame  = self.driver.find_element(By.XPATH,f"//div[@class={WEB_FRAME_FOLLOWERS_FOLLOWING}]")
        scroll_origin = ScrollOrigin.from_element(frame)
        
        #Where we save the name
        names =  set({})
        
        salto = 50


        while len(names)+1<total_followers_or_following:
            
            elements = self.driver.find_elements(By.XPATH, f"//*[@class={WEB_NAME_FOLLOWERS_FOLLOGIN}]")
                
            for element in elements:
                names.add(element.text)
                  
            ActionChains(self.driver)\
            .scroll_from_origin(scroll_origin,0,int(salto))\
            .perform()
            
            salto+=4
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

     
    """
    Check who view your history and not is follower about your account.
    
    """
    def seeVisitedHistory(self):
        
        
        #Check if exist the followers list
        if not (os.path.exists(ROUTE_FILE_FOLLOWERS_OLDER)):
            self.modelStart(True,True)
        
        #URL of the stories archive that could scan
        self.driver.get()

        element = self.driver.find_element(By.XPATH, "//span[@class='xfungia x1yxbuor x19qstwj x1yrs1ss']")
        element.click()
        time.sleep(4)

        frame  = self.driver.find_element(By.XPATH,f"//div[@class={WEB_FRAME_VIWED_HISTORY}]")
        scroll_origin = ScrollOrigin.from_element(frame)
        lastElementName=""
        tryAagain = True
    

        while True:
            
            names = self.driver.find_elements(By.XPATH, f"//span[@class={WEB_NAME_VIWED_HISTORY}]")
            
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
        names = self.driver.find_elements(By.XPATH, f"//span[@class={WEB_NAME_VIWED_HISTORY}]")

        for name in names:
            self.views.add(name.text)

            
        lista_file_old = []
        
        with open(ROUTE_FILE_FOLLOWERS_OLDER) as file:
            for line in file:
                lista_file_old.append(line.replace("\n",""))

        file = open("non_followers_view.txt",'w')
        
        for view in self.views:
            if not view in lista_file_old:
                file.write(f"No té sigue -> {view}\n")
                print(f"No té sigue -> {view}")
                
    def checkNotFollowBack(self):
        
       # self.modelStart(True,True)
        #self.modelStart(False,True)
        
        followers = []
        
        with open(ROUTE_FILE_FOLLOWERS_OLDER) as file:
            for line in file:
                followers.append(line.replace("\n",""))

        followings = []
        
        with open(ROUTE_FILE_FOLLOWING_OLDER) as file:
            for line in file:
                followings.append(line.replace("\n",""))
                
        
        for user_following in followings:
            if not user_following in followers:
                print(user_following)

