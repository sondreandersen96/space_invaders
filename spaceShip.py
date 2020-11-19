'''
The SpaceShip has a size of 30x30 pixels. 
'''
from laser import Laser

class SpaceShip:
    def __init__(self, icon, pos_x, pos_y):
        self._icon = icon 
        self._pos_x = pos_x
        self._pos_y = pos_y 
        self._width = 30
        self._height = 30
        self._speed = 10

    # Test if the spaceship has hit the wall on either side,
    # .. returns True if is has, False otherwise. 
    def hitWallLeft(self):
        if self._pos_x <= 0 + 20:
            return True
        else:
            return False 

    def hitWallRight(self, WIDTH):
        if self._pos_x + self._width >= WIDTH - 20:
            return True
        else:
            return False 

    def moveRight(self):
        self._pos_x += self._speed

    def moveLeft(self):
        self._pos_x -= self._speed

    def fireLaser(self):
        new_laser = Laser((self._pos_x + self._width / 2), self._pos_y, 7)
        return new_laser

    def render(self, screen):
        screen.blit(self._icon, (self._pos_x, self._pos_y))
