import random


class Card:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The value of the card that is reveal (from 1 to 13)
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Die): An instance of Card.
        """
        self.value = random.randint(1, 13)
        self.points = 0

    def reveal(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1, 13)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0

        # if (guess == 'h' or guess == 'H') and (self.card_1 < self.card_2):

        #     new_player.score += 100

        # elif (guess == 'l' or guess == 'L') and (self.card_1 > self.card_2):

        #     new_player.score += 100

        # else:

        #     new_player.score -= 75
        #     new_player.check_score()