from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        #Gets the two score classes from the scores group...
        # scores_list = cast.get_actors("scores")
        # player_one_score = cast.get_first_actor("scores")
        # player_two_score = scores_list[1]


        #Gets the two snake classes from the snakes group...
        snakes_list = cast.get_actors("snakes")
        player_one = snakes_list[0]
        player_two = snakes_list[1]


        food = cast.get_first_actor("foods")
        player_one_segments = player_one.get_segments()
        player_two_segments = player_two.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        # self._video_service.draw_actor(food)
        self._video_service.draw_actors(player_one_segments)
        self._video_service.draw_actors(player_two_segments)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()