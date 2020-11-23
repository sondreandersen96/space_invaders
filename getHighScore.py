'''
This is a helper function that gets the current high score
if a file called highscore.txt exist, otherwise it returns 
False. 
'''

def getHighScore():
    try:
        highScoreFile = open('highscore.txt', 'r')
        highScore = highScoreFile.read().strip()
        highScoreFile.close()
        return int(highScore)
    except:
        return False 
