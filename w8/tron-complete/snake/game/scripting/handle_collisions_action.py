import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._player_that_won = False
        # Player that won is true if player one wins, false if player two wins. This can be used to determine a 
        # message to players when game over happens
    

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        pass
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = 1
        players = cast.get_actors("snakes")

        snake_1 = players[0]
        snake_2 = players[1] # Change its starting position, color, controls,...etc

        if True:
            # points = food.get_points()
            snake_1.grow_tail(score)
            snake_2.grow_tail(score)

            # score.add_points(points)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        players = cast.get_actors("snakes")

        snake_1 = players[0]
        snake_2 = players[1]
        head_1 = snake_1.get_segments()[0]
        head_2 = snake_2.get_segments()[0]

        segments_1 = snake_1.get_segments()[1:]
        segments_2 = snake_2.get_segments()[1:]

        
        for segment in segments_1:
            if head_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments_2:
            if head_1.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments_1:
            if head_2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for segment in segments_2:
            if head_2.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            players = cast.get_actors("snakes")

            snake_1 = players[0]
            snake_2 = players[1] 
            segments_1 = snake_1.get_segments()
            segments_2 = snake_2.get_segments()

            # food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments_1:
                segment.set_color(constants.WHITE)
            
            for segment in segments_2:
                segment.set_color(constants.WHITE)
            # food.set_color(constants.WHITE)