import constants

from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.snake import Snake
from game.casting.snake2 import Snake2

from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.control_actors_action2 import ControlActorsAction2

from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    # cast.add_actor("foods", Food())s

    #Players

    cast.add_actor("snakes", Snake())
    cast.add_actor("snakes", Snake2())

    players = cast.get_actors("snakes")

    snake_1 = players[0]
    snake_2 = players[1] # Change its starting position, color, controls,...etc

    snake_1.set_position(Point(300, 300))
    snake_2.set_position(Point(700, 600))
    # snake_2.set_color(255, 0, 0)


    # =====================


    # #Adds scores to the game...
    # cast.add_actor("scores", Score())
    # cast.add_actor("scores", Score())

    # #Gets the two scores...
    # player_scores = cast.get_actors("scores")



    # #Assigns the players to their scores in the list..
    # player_1_score = player_scores[0]
    # player_2_score = player_scores[1]


    # player_2_score.set_text('Player 2:')
    # player_2_score.set_position(Point(800, 0))
    


    # #Sets the text of the score on screen
    # player_1_score.set_text('Player 1:')
    # player_1_score.set_position(Point(0, 0))

    print("===================================")
    print(cast.get_all_actors())
    print("===================================")



    # start the gamekl
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("input", ControlActorsAction2(keyboard_service))
    script.add_action("update", HandleCollisionsAction())
    # script.add_action('update', TronTailAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()