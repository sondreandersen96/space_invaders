from spaceShip import SpaceShip
from gameController import GameController
from random import randint
WIDTH = 800
HEIGHT = 600
'''
Run program with pgzrun main.py

'''


# Setup
#                                #  X         Y 
#ship = SpaceShip('space_ship.png', 400 - 15, 525 - 15)
game = GameController(WIDTH, HEIGHT)



def draw():
    screen.fill((10, 10, 10))

    # Draw main ship 
    game.renderSpaceShip(screen)

    # Draw lasers 
    game.renderLasers(screen)
    game.renderEnemies(screen)

    screen.draw.text(f'Count: {game.getCount()}', [10, 10])


def update():



    # Move Spaceship
    game.handleSpaceShipActions(keyboard)




    # Handle lasers
    game.moveLasers()
    game.removeOffscreenLasers()





    # Handle enemies
    if game.getCount() == 0:
        game.createRowOfEnemies(4, 1)
    elif game.getCount()%200 == 0:
        game.shiftEnemiesOneRowDown()
        randomNrOfEnemies = randint(2, 12)
        game.createRowOfEnemies(randomNrOfEnemies, 1)

    game.checkStatusEnemies()        







    # Handle laser hits
    game.detectLaserHit()





    # Frame counter
    game.increaseCounter()




    # Prototyping.......
    if keyboard.a:
        game.createRowOfEnemies(16, 1)
    if keyboard.s:
        game.createRowOfEnemies(3, 1)
    if keyboard.x:
        game.shiftEnemiesOneRowDown()









