from model import SeleniumInstagram
from view import View
from controller import Controller_Instagram
import time
import threading
from pynput.keyboard import Key, Controller,Listener

model_one = SeleniumInstagram()
model_two = SeleniumInstagram()
view = View()


controller = Controller_Instagram(seleniumInstagram=model_one,view=view)

def on_press(key):
    if key== Key.ctrl:
        
        hilo_followers = threading.Thread(target=model_one.modelStartAnalyseFollowers,args=(True,))
        hilo_following = threading.Thread(target=model_two.modelStartAnalyseFollowers,args=(False,))
        

        hilo_following.start()
        hilo_followers.start()
       
        hilo_following.join()
        hilo_followers.join()

        controller.listaFollowers = model_one.followers
        controller.listaFollowing = model_two.followers

        controller.show()

        
        
        
    
with Listener(on_press=on_press) as listener:
    listener.join()



while True:
    pass
    