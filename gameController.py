from spaceShip import SpaceShip

class GameController:
    def __init__(self):
        self._counter = 0 
        self._score = 0 
        self.spaceship = SpaceShip('space_ship.png', 400 - 15, 525 - 15)
        self._lasers = []
        

    def increaseCounter(self):
        self._counter += 1 


    def addLaser(self, laser):
        if self._counter % 2 == 0:
            self._lasers.append(laser)

    def renderLasers(self, screen):
        for laser in self._lasers:
            laser.render(screen)

    def moveLasers(self):
        for laser in self._lasers:
            laser.move()

    def removeOffscreenLasers(self):
        for laser in self._lasers:
            if laser.isOffScreen():
                self._lasers.remove(laser)

