from Words.py import Words
from Stickman.py import Stickman
from Commander.py import Commander

class Terminal():
    
    def __init__(self):

        self.user_guess = input('Guess a letter [a-z]: ') #May need to add something to make sure the correct values are put in.

    
    def print_hidden_word(self): 
        
        #This will print the underscores of the hidden word to the console inside of a list.
        #This is so we can reference the list and replace underscores with the actual guessed letter.

        hidden_word_underscores = []

        for i in Words.word_length: #Loops through the word in the Word Class. For every letter it will add an _ to the hidden_word_underscores list.

            hidden_word_underscores.append("_" + " ") #Adds underscores to the hidden_word_underscores list. And a space to make it more readable: ____ vs. _ _ _ _ (Remember that it will affect index.)
        
        print(hidden_word_underscores)

    # def show_hidden_word(self): #Prints the hidden_word_underscores, the _ will be replaced with the letter from the word.



    def check_word(self): #Checks the user input against a word 

        #THE MOST IMPORTANT PART OF THE PROGRAM!!!! -
        # This is how it's setup:
        # list of underscores: _ _ _ _ _
        # ----The hidden word: M O O S E

        #If the [USER INPUT] is in [HIDDEN WORD]:
        #Get the index of the letter in hidden word. And replace the _ in the underscore list with the same index, with the letter
        # Below is a rough outline, it's not finished.



        if self.user_guess in Words.random_word: #If the user input is inside the random word...
            
            letter = self.user_guess
            # Put the logic of replacing the word in the Underscore_list here:...
            # Find the index of the letter in the hidden word...


            self.show_hidden_word()
            Stickman.draw_stickman() #Draws the stickman again 
            self.user_guess
            self.check_end_game() #Checks if the game needs to end.

        else:
            
            Stickman.remove_section #Removes a section from the stickman.
            Stickman.lives -= 1 #Takes away a life from the stickman's lives.
            self.show_hidden_word() #Shows the hidden word.
            Stickman.draw_stickman() #redraws the stickman after a section ^^^ has been removed.




            self.check_end_game() #Checks if the game needs to end.


    def check_end_game(self):

        if Stickman.lives <= 0: #Ends the game if the stickman's lives hit zero.

            Commander.end_game()

        elif "_" in hidden_word_underscores: #Checks if there are underscores in the underscore list, if there are it means that the game should continue. 

            pass

        else:

            Commander.end_game() #if there are no underscores left in the underscore list and there are still lives left, the user wins, ends the game.




