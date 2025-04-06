from selenium import webdriver
import pickle
from pynput.keyboard import Key, Controller,Listener

driver = webdriver.Chrome()
from constants import ROUTE_FILE_OUR_COOKIES,BASE_URL
#navigate to the url


driver.get(BASE_URL)

def save_our_cookies():
        
    #create a variable to hold our cookies
    cookies = driver.get_cookies()

    #print the cookies list
    n = 1
    for cookie in cookies:
        pickle.dump(cookie,open(f"{ROUTE_FILE_OUR_COOKIES}cookie{n}.pkl", "wb"))
        print(f"Saved {n}")
        n+=1
        

    #close the browser
    driver.quit()

def tryEntre():
    
    for x in range(1,9):
        print(f"{ROUTE_FILE_OUR_COOKIES}cookie{x}.pkl")
        cookies = pickle.load(open(f"{ROUTE_FILE_OUR_COOKIES}cookie{x}.pkl","rb"))
        
        
        driver.add_cookie(cookies)
    
    driver.refresh()



def on_press(key):
    if key== Key.ctrl:
        save_our_cookies()
    if key== Key.alt:
        tryEntre()

with Listener(on_press=on_press) as listener:
    listener.join()



while True:
    pass
    