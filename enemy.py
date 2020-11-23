'''
This class creates enemy characters in the game. 

The following characteristics can be changed for each enenmy:
- maxDamage
- Icon 
- Points for taking out enemy
    

For the following points are awarded for taking out an enemy at a specific level:
1. 10 (Easy Enemy)

'''

class Enemy:
    def __init__(self, icon, pos_x, pos_y, width, height, maxDamage, hitPoints):
        self._icon = icon 
        self._pos_x = pos_x
        self._pos_y = pos_y 
        self._width = 30
        self._height = 30
        self._maxDamage = maxDamage
        self._damage = 0 
        self._hitPoints = hitPoints
    
    def move(self):
        self._pos_y += 45
    
    def detectHitFromLaser(self, laser):
        laser_pos_x = laser.getPosAndRadius()[0]
        laser_pos_y = laser.getPosAndRadius()[1]
        laser_radius = laser.getPosAndRadius()[2]

        if (laser_pos_x - laser_radius >= self._pos_x) and (laser_pos_x + laser_radius <= self._pos_x + self._width):
            if (self._pos_y + self._height >= laser_pos_y + 2):
                return True 
        return False 

    def hit(self):
        self._damage += 1 

    def getDamage(self):
        return self._damage

    def getMaxDamage(self):
        return self._maxDamage

    def hasReachedPlayer(self):
        if self._pos_y >= 520:
            return True
        else:
            return False 

    def getHitPoints(self):
        return self._hitPoints


    def render(self, screen):
        screen.blit(self._icon, (self._pos_x, self._pos_y))
