from random import choice

class game:
    win=0
    draw=0
    lose=0
    def __init__(self,com_input,user_input):
        self.com_input=com_input
        self.user_input=user_input
    
    def result(self):
        if self.win>self.draw and self.win>self.lose:print("you have won")
        elif self.draw>self.win and self.draw>self.lose:print("game is draw")
        else:print("you lose")

    def run_game(self):
        if self.com_input==self.user_input:
            self.draw+=1
        elif self.user_input=="snake":
            if self.com_input=="water":
                self.win+=1
            elif self.com_input=="gun":
                self.lose+=1
        elif self.user_input=="water":
            if self.com_input=="snake":
                self.lose+=1
            elif self.com_input=="gun":
                self.win+=1
        elif self.user_input=="gun":
            if self.com_input=="water":
                self.lose+=1
            elif self.com_input=="snake":
                self.win+=1
        

while(True):       
    user_inp=input("enter from snake water or gun >")
    com_inp=choice(["snake","water","gun"])
    print(f"computer has choosen {com_inp}")
    
    if not user_inp:
        snw.result()
        break
    snw=game(com_inp,user_inp)
    snw.run_game()
