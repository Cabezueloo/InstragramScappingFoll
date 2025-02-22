from model import SeleniumInstagram
from view import View
from controller import Controller_Instagram
import time
import threading
from pynput.keyboard import Key, Controller,Listener

model_one = SeleniumInstagram()
model_two = SeleniumInstagram()
model_three = SeleniumInstagram()
view = View()


controller = Controller_Instagram(seleniumInstagram=model_one,view=view)

def on_press(key):
    if key== Key.ctrl:
        
        hilo_followers = threading.Thread(target=model_one.modelStartAnalyseFollowers,args=(True,))
        hilo_following = threading.Thread(target=model_two.modelStartAnalyseFollowers,args=(False,))
        hilo_views = threading.Thread(target=model_three.seeVisitedHistory)
        
        t = time.time()
        hilo_following.start()
        hilo_followers.start()
        hilo_views.start()
       
        hilo_following.join()
        hilo_followers.join()
        hilo_views.join()
        
        print(f"Tiempo en coger todas las estadísticas {time.time() - t} ")

        controller.listaFollowers = model_one.followers
        controller.listaFollowing = model_two.followers
        controller.listaViews = model_three.views

        controller.show_stats()
        controller.users_saw_history_and_not_follow_your_account()
        controller.users_not_follow_back()

        
        
        
    
with Listener(on_press=on_press) as listener:
    listener.join()



while True:
    pass
    