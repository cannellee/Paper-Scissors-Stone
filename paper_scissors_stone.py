from random import*

class PFC():
    def __init__(self):
        print("P - pierre | F - feuille | C - ciseaux | Q - arrêter")
        self.choice_robot=input("Jouer contre un robot (R) : ")
        self.choice_robot=self.choice_robot.upper()
        self.choice_player_one=""
        self.choice_player_two=""
        self.score_player_one=0
        self.score_player_two=0
        self.winner=0
        self.choices=["F", "P", "C"]
        self.main()


    def main(self):
        if self.choice_robot=="R":
            self.choice_player_one=self.choices[randint(0, 2)]
        else:
            self.choice_player_one=input("Choix joueur 1 :")
            self.choice_player_one=self.choice_player_one.upper()
        self.choice_player_two=input("Choix joueur 2 :")
        self.choice_player_two=self.choice_player_two.upper()
        
        if self.choice_player_two=="Q" or self.choice_player_one=="Q":
            if self.score_player_one<self.score_player_two:
                self.winner=2
            elif self.score_player_one>self.score_player_two:
                self.winner=1
            else:
                self.winner="... ET NON, c'est une égalité"
            print("Merci d'avoir joué ! Voici les scores : \n Joueur 1 :", self.score_player_one, "\n Joueur 2 :", self.score_player_two, "\n Bravo au joueur", self.winner, "!!")
        elif self.choice_player_one==self.choice_player_two:
            print("Egalité sur cette manche !")
            self.main()
        elif self.choice_player_one not in self.choices or self.choice_player_two not in self.choices:
            print("Veuillez mettre une lettre valide")
            self.main()
        else:
            for i in range(len(self.choices)):
                if self.choice_player_one==self.choices[i]:
                    if i==2:
                        i=-1
                    if self.choice_player_two==self.choices[i+1]:
                        self.score_player_one+=1
                        print("Joueur 1 a gagné cette manche !")
                    else:
                        self.score_player_two+=1
                        print("Joueur 2 a gagné cette manche !")
                    self.main()

pfc=PFC()
