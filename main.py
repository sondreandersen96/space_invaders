from spaceShip import SpaceShip
from gameController import GameController
from setHighScore import setHighScore
from random import randint
'''
Run program with pgzrun main.py

'''


WIDTH = 800
HEIGHT = 600


# Setup
game = GameController(WIDTH, HEIGHT)
gameOver = False 
haveTestedForHighScore = False # Global variable
newHighScoreEvent = False # Global variable 



# Pygame Zero Functions - Game Loops
def draw():
    if not gameOver:
        inGameGraphics()
    else:
        gameOverScreen()

def update():
    if not gameOver:
        inGameUpdate()




# Game logic functions 
def inGameGraphics():
    screen.fill((10, 10, 10))
    # Draw main ship 
    game.renderSpaceShip(screen)

    # Draw lasers 
    game.renderLasers(screen)
    game.renderEnemies(screen)

    screen.draw.text(f'Frame Count: {game.getCount()}', [350, 10])
    screen.draw.text(f'Score: {game.getScore()}', [10,10])
    screen.draw.text(f'Level: ', [150, 10])


def inGameUpdate():
    # Move Spaceship
    game.handleSpaceShipActions(keyboard)

    # Handle lasers
    game.moveLasers()
    game.removeOffscreenLasers()

    # Handle enemies
    if game.getCount() == 0:
        game.createRowOfEnemies(4, 1)
    elif game.getCount()%100 == 0:
        game.shiftEnemiesOneRowDown()
        randomNrOfEnemies = randint(2, 12)
        game.createRowOfEnemies(randomNrOfEnemies, 1)

    game.checkStatusEnemies()        

    # Handle laser hits
    game.detectLaserHit()

    # Frame counter
    game.increaseCounter()

    # Check for game over event 
    if game.detectGameOver():
        global gameOver
        gameOver = True
        print('Game Over Event Detected')


    # Prototyping.......
    if keyboard.a:
        game.createRowOfEnemies(16, 1)
    if keyboard.s:
        game.createRowOfEnemies(3, 1)
    if keyboard.x:
        game.shiftEnemiesOneRowDown()



def gameOverScreen():
    screen.fill((20,20,20))
    score = game.getScore()
    previousHighScore = game.getPreviousHighScore()

    '''
    I am using these global variables to aviod having to 
    test for new high score on every frame after the game 
    has ended. With this code, once a high score is detected
    we dont need to test for a high score anymore, we just 
    have to render the high score screen. 
    '''
    global haveTestedForHighScore
    global newHighScoreEvent

    if (previousHighScore < score) and (not haveTestedForHighScore):
        newHighScoreEvent = True
        setHighScore(score) # Saving new high score to file 
        haveTestedForHighScore = True
        newHighScoreEvent = True



    if newHighScoreEvent: 
        # New High Score Screen
        screen.draw.text('NEW HIGH SCORE!', [250, 180], color=(0, 240, 0))
        screen.draw.text(f'SCORE: {score}', [250, 220])
        screen.draw.text(f'Previous High Score was: {previousHighScore}', [250, 260])
        
    else:
        screen.draw.text('GAME OVER!', [250, 180], color=(240, 0, 0))
        screen.draw.text(f'Score: {score}', [250, 220])
        screen.draw.text(f'Current High Score is: {previousHighScore}', [250, 260])


