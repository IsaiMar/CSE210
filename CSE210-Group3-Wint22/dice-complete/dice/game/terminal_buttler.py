from Words.py import Words

class Terminal_Butler():

    """A service that handles terminal operations.
    
    The responsibility of a Terminal_Butler is to provide correct input and output operations for the 
    commander, stickman, and words classes.
    """
     
    def check_letter(self, guess, list, i=0):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        while guess == list[i]:
            return guess

        else:
            return input("Guess a letter [a-z]: ")


    # def read_number(self, prompt):
    #     """Gets numerical input from the terminal. Directs the user with the given prompt.

    #     Args: 
    #         self (TerminalService): An instance of TerminalService.
    #         prompt (string): The prompt to display on the terminal.

    #     Returns:
    #         float: The user's input as a number.
    #     """
    #     return float(input(prompt))
        
    # def write_text(self, text):
    #     """Displays the given text on the terminal. 

    #     Args: 
    #         self (TerminalService): An instance of TerminalService.
    #         text (string): The text to display.
    #     """
    #     print(text)
        
    # #responsibilities: error handling, run inputs (check its a letter - not a number or unknown symbol)


    # pass