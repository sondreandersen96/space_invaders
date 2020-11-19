class Laser:
    def __init__(self, start_x, start_y, speed):
        self._pos_x = start_x 
        self._pos_y = start_y 
        self._speed = speed

    def move(self):
        self._pos_y -= self._speed

    def render(self, screen):
        screen.draw.circle((self._pos_x, self._pos_y), 2, (255,255,255))

    def isOffScreen(self):
        if self._pos_y <= 50:
            return True
        else:
            return False 