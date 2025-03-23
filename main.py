from model import SeleniumInstagram
from view import View
from controller import Controller_Instagram
import time
import threading
from pynput.keyboard import Key, Controller,Listener

model = SeleniumInstagram()

view = View()


controller = Controller_Instagram(seleniumInstagram=model,view=view)

def on_press(key):

    if key== Key.ctrl:
        
        hilo = threading.Thread(target=model.modelStart,args=(True,True))
    
        t = time.time()
    
        hilo.start()
 
        hilo.join()
   
        print(f"Tiempo en coger todas las estadísticas {time.time() - t} ")

        print("fIN")

        
        
        
    
with Listener(on_press=on_press) as listener:
    listener.join()



while True:
    pass
    