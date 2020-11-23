'''
This is a helper function that takes in the new highscore 
as an argument and stores that highscore in a file called
highscore.txt

'''

def setHighScore(highscore):
    f = open('highscore.txt', 'w')
    f.write(str(highscore))
    f.close()

