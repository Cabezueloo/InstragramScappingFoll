from model import SeleniumInstagram
from view import View

class Controller_Instagram:

    def __init__(self, seleniumInstagram:SeleniumInstagram,view:View):
        self.seleniumInstragramController = seleniumInstagram
        self.viewController = view
        self.listaFollowers = []
        self.listaFollowing = []
    
    def controllerStartAnalyse(self) : self.seleniumInstragramController.modelStartAnalyse()

    def show(self):
        print(f"Tamagno followers -> {len(self.listaFollowers)}")
        print(f"Tamagno following -> {len(self.listaFollowing)}")