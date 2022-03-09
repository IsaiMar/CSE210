from game.casting.actor import Actor
from game.shared.point import Point


class Artifact(Actor):
    
    
    def __init__(self):

        super().__init__()    
        
        
    def move_next(self, max_x, max_y):
       
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y + 5
        self._position = Point(x, y)