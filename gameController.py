from spaceShip import SpaceShip
from enemy import Enemy 



class GameController:
    def __init__(self, WIDTH, HEIGHT):
        self._WIDTH = WIDTH # Screen width 
        self._HEIGHT = HEIGHT # Screen height
        self._counter = 0 
        self._score = 0 
        self._spaceship = SpaceShip('space_ship.png', 400 - 15, 560 - 15)
        self._lasers = []
        self._enemies = []

    def increaseCounter(self):
        self._counter += 1 

    def addLaser(self, laser):
        if self._counter % 2 == 0:
            self._lasers.append(laser)

    def renderLasers(self, screen):
        for laser in self._lasers:
            laser.render(screen)

    def renderSpaceShip(self, screen):
        self._spaceship.render(screen)

    def renderEnemies(self, screen):
        for enemy in self._enemies:
            enemy.render(screen)

    def moveLasers(self):
        for laser in self._lasers:
            laser.move()

    def shiftEnemiesOneRowDown(self):
        for enemy in self._enemies:
            enemy.move()

    def createEasyEnemy(self, pos_x, pos_y):
        new_enemy = Enemy('enemy_1.png', pos_x, pos_y, 30, 30, 2, 10) # icon, pos_x, pos_y, width, height, maxDamage
        self._enemies.append(new_enemy)

    def createRowOfEnemies(self, nr, typeOfEnemy): # Spesify the number of enemies to be created (max 16) 
        midPoint = self._WIDTH / 2 
        space_for_one_enemy = 30 + 15
        start_pos = midPoint - ((nr / 2) * (space_for_one_enemy))
        
        pos_x = start_pos
        for i in range(nr):
            if typeOfEnemy == 1: # Easy level
                self.createEasyEnemy(pos_x, 100)
                pos_x += space_for_one_enemy

    def removeOffscreenLasers(self):
        for laser in self._lasers:
            if laser.isOffScreen():
                self._lasers.remove(laser)

    def handleSpaceShipActions(self, keyboard):
        if keyboard.left:
            if not self._spaceship.hitWallLeft():
                self._spaceship.moveLeft()

        if keyboard.right:
            if not self._spaceship.hitWallRight(self._WIDTH):
                self._spaceship.moveRight()

        if keyboard.up or keyboard.space:
            new_laser = self._spaceship.fireLaser()
            self.addLaser(new_laser)

    def detectLaserHit(self):
        for enemy in self._enemies:
            for laser in self._lasers:
                if enemy.detectHitFromLaser(laser):
                    self._lasers.remove(laser)
                    self._score += enemy.getHitPoints()
                    enemy.hit()
                    

        
    def checkStatusEnemies(self):
        enemiesToRemove = []
        # Finding enemies to remove
        for enemy in self._enemies:
            if enemy.getDamage() >= enemy.getMaxDamage():
                enemiesToRemove.append(enemy)
        # Removing enemies that have a damage level higher than max. 
        for enemy in self._enemies:
            if enemy in enemiesToRemove:
                self._enemies.remove(enemy)


    def detectGameOver(self): # Defined as when an enemy reaches the player 
        for enemy in self._enemies:
            if enemy.hasReachedPlayer():
                return True
        return False 


    def getCount(self):
        return self._counter

    def getScore(self):
        return self._score
    
