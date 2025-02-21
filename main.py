from model import SeleniumInstagram
from view import View
from controller import Controller_Instagram
import time
from pynput.keyboard import Key, Controller,Listener

model = SeleniumInstagram()
view = View()


controller = Controller_Instagram(seleniumInstagram=model,view=view)

def on_press(key):
    if key== Key.ctrl:
        model.modelStartAnalyseFollowers()
    
with Listener(on_press=on_press) as listener:
    listener.join()



while True:
    pass
    