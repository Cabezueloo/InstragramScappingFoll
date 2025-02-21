from selenium import webdriver
import pickle
from pynput.keyboard import Key, Controller,Listener

driver = webdriver.Chrome()

#navigate to the url

ROUTE_COOKIES = "cookie_login/"
driver.get("https://www.instagram.com/")

def showCookie():
        
    #create a variable to hold our cookies
    cookies = driver.get_cookies()

    #print the cookies list
    n = 9
    for cookie in cookies:
        pickle.dump(cookie,open(f"{ROUTE_COOKIES}cookie{n}.pkl", "wb"))
        print(f"Saved {n}")
        n+=1
        

    #close the browser
    driver.quit()

def tryEntre():
    
    for x in range(1,9):
        print(f"{ROUTE_COOKIES}cookie{x}.pkl")
        cookies = pickle.load(open(f"{ROUTE_COOKIES}cookie{x}.pkl","rb"))
        
        
        driver.add_cookie(cookies)
    
    driver.refresh()



def on_press(key):
    if key== Key.ctrl:
        showCookie()
    if key== Key.alt:
        tryEntre()

with Listener(on_press=on_press) as listener:
    listener.join()



while True:
    pass
    