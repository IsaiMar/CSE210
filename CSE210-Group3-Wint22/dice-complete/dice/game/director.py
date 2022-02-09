from game.die import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.current_card = 0
        self.is_playing = True
        self.total_score = 300

        # for i in range(5):
        #     die = Die()
        #     self.dice.append(die)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.show_card()
            self.do_updates()
            self.do_outputs()
            self.get_inputs()

    def show_card(self):
        if not self.is_playing:
            return 
        card = self.card 
        print(f"The card is: {card.value}")
        
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        guess = input('Higher or lower? (h/l): ')
        card = self.card
        card.reveal()
        self.total_score += card.points

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        # values = ""
        # for i in range(len(self.dice)):
        #     die = self.dice
        #     values += f"{die.value} "

        # print(f"You rolled: {values}")
        print(f"Next card was:{current_card}\n")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play_again = input("Play again? [y/n] ")
        self.is_playing = (play_again == "y")



