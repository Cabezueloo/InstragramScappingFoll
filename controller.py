from model import SeleniumInstagram


STATS : str = 'stats/'

class Controller_Instagram:

    def __init__(self, seleniumInstagram:SeleniumInstagram):
        self.seleniumInstragramController = seleniumInstagram
        
        self.listaFollowers = []
        self.listaFollowing = []
        self.listaViews = []
    
    #def controllerStartAnalyse(self) : self.seleniumInstragramController.modelStartAnalyse()

    def users_saw_history_and_not_follow_your_account(self):
        
        route = STATS+"usersSawHistoryNotFollowYourAccount.txt"
        f = open(file=route+"",mode='w')

        for user in self.listaViews:
            if not user in self.listaFollowers:
                #print(f"El usuario {user} no te sigue y te ha visto la historia")
                f.write(f"El usuario {user} no te sigue y te ha visto la historia\n")
        
        f.close()
    
    def users_not_follow_back(self):

        route = STATS+"usersNotFollowBack.txt"
        f = open(route,mode='w')

        for follow in self.listaFollowing:
            print(follow)
            print(f"Me sigue -> {follow in self.listaFollowers}")
            if not follow in self.listaFollowers:
                f.write(f"El usuario {follow} no te sigue de vuelta\n")
        f.close()

        

    

    

