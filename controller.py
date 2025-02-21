from model import SeleniumInstagram
from view import View

class Controller_Instagram:

    def __init__(self, seleniumInstagram:SeleniumInstagram,view:View):
        self.seleniumInstragramController = seleniumInstagram
        self.viewController = view
    
    def controllerStartAnalyse(self) : self.seleniumInstragramController.modelStartAnalyse()