from gameplay.cards import cards


class thrower:

    """This class in meant to organize the game"""

    def hilo(self):

        self.cards = cards()
        self.play = False
        self.score = 0
        self.fist_card = 0
        self.next_card = 0
        self.guess = ""

    def start(self):
        """This Starts the game"""

        self.playerpoints = 300
        self.play = True

        while self.play and self.playerpoints > 0:
            self.get_guess()
            self.do_logic()
            self.do_display()

    def get_guess(self):
        """ This funciton displays the first card and takes the player's guess 
            (high or low card) as an input"""
        # I had to add this call and identifier here. "cards()" class wasn't recognized in this function. 
        self.cards = cards()

        self.first_card = self.cards.draw()
        print(f"The card is: {self.first_card}")

        self.guess = input(f"High or Low? [h/l]").lower()

        # Instead of the number "1", had to change to letter "l" here... 
        while self.guess != "h" and self.guess != "l":
            print("Invalid selection, please try again. ")
            self.guess = input(f"High or Low? [h/l]").lower()
        self.next_card = self.cards.draw()

        print(f"Next card was: {self.next_card}")

    def do_logic(self):
        "This function keeps track of the score"

        # ...and here 
        if self.guess == "l":
            if self.next_card <= self.first_card:
                self.playerpoints += 100
            else:
                self.playerpoints -= 75
        elif self.guess == "h":
            if self.next_card >= self.first_card:
                # minor mistake, from player_points to playerpoints 
                self.playerpoints += 100
            else:
                self.playerpoints -= 75
        elif self.playerpoints < 75:                    # similar as above.
            self.play = False

    def do_display(self):
        """This functions prints the results and if the score isn't 0, it will ask if user wants to play again"""

        print(f"Your score is: {self.playerpoints}")        # just a typo. 

        self.playagain = input(f"Do you want to keep playing? [y/n]").lower()

        while self.playagain != "y" and self.playagain != "n":
            print("Invalid selection, please try again. ")
            self.playagain = input(f"Do you want to keep playing? [y/n]").lower()

        if self.playagain == "n":
            self.play = False
        elif self.playagain == "y":
            self.play = True

        if self.play == False:
            print("Game Over! Thanks for playing!")
            print(f"Your final score was {self.playerpoints}")
