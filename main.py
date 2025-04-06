from model import SeleniumInstagram
from controller import Controller_Instagram
import time
import threading
from pynput.keyboard import Key, Controller,Listener
import os

model = SeleniumInstagram()
continuar = True
controller = Controller_Instagram(seleniumInstagram=model)

def on_press(key):
    global continuar
    if key== Key.ctrl:
        
        #Create folders
        if not (os.path.isdir('following')):
            os.makedirs('following')
        if not (os.path.isdir('followers')):
            os.makedirs('followers')

        
        searchBy : bool= int(input("Quieres buscar por followers o following? (1 o 2)"))==1
        firstScann : bool= input("Es el primer escaneo? (s/n)")=='s'
        
        
        t = time.time()
        model.modelStart(searchBy,firstScann)
    
        print(f"Tiempo en coger todas las estadísticas de followers/following {time.time() - t} ")

        print("FIN")

    #If press KEY ALT, you can check the users that not following you and see you history
    if key== Key.alt:

        t = time.time()
        model.seeVisitedHistory()
        print(f"Tiempo en coger todas las estadisticas de la historia {time.time() - t} ")
        print("fIN")
    
    if key == Key.shift:
        t = time.time()
        model.checkNotFollowBack()
        print(f"Tiempo en coger todas las estadisticas de la historia {time.time() - t} ")
        print("fIN")
    
    if key== Key.esc:
        model.driver.close()
        continuar = False
                
    
with Listener(on_press=on_press) as listener:
    listener.join()

while continuar:
    pass
    
exit(1)