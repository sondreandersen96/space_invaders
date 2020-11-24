# The level system in the game



## Moving up the level system 
The player moves up one level for each 1000 points recieved. 

This is controlled by the GameController instance function `handleLevels()`.


## The Nature of the Level System 
Three types of enemies exist in this game.

As the player moves up the levels of the game, a higher probability is assigned to high level enemies apoearing. The exact probabilities are described in the file "levelSystem.csv", which is the file the game controller used to find the probability of what type of enemy is created on the new row. 


| Enemy Level | Max Damage | Image File  |
|-------------|------------|-------------|
| 1           | 2         | enemy_1.png |
| 2           | 5          | enemy_2.png |
| 3           | 8          | enemy_3.png |


The "levelSystem.csv" file has the following headers: 

level; probability of enemy 1; probability of enemy 2; probability of enemy 3 


When the GameController class is initiated at the start of the game, this level system is read and stored as a dictionary in an instance variable. The dictionary is of the format:

| Key | Value | 
|-------------|------------|
| Level           | [probEnemy1, probEnemy2, probEnemy3]  | 




The way the game is created now, it will crash at above level 200.....

