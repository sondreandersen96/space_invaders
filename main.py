from spaceShip import SpaceShip
from gameController import GameController
WIDTH = 800
HEIGHT = 600
'''
Run program with pgzrun main.py

'''


# Setup
#                                #  X         Y 
#ship = SpaceShip('space_ship.png', 400 - 15, 525 - 15)
game = GameController()



def draw():
    screen.fill((10, 10, 10))

    # Draw main ship 
    ship.render(screen)

    # Draw lasers 
    game.renderLasers(screen)

def update():



    # Move Spaceship
    if keyboard.left:
        if not ship.hitWallLeft():
            ship.moveLeft()
    if keyboard.right:
        if not ship.hitWallRight(WIDTH):
            ship.moveRight()
    if keyboard.up:
        new_laser = ship.fireLaser()
        game.addLaser(new_laser)




    # Handle lasers
    game.moveLasers()
    game.removeOffscreenLasers()



    game.increaseCounter()




