# Pygame Zero Space Invaders 

This is a replica of the classical Space Invaders Game, created using Pygame Zero, with an object oriented programming approach.

![Demo Image](demo_image1.png)

To run the game:
```
pgzrun main.py  
```

**The game is still very much a work in progress, but some simple functionallity is implemented:**
- Move SpaceShip
- Fire lasers from SpaceShip
- Create weak (low level) Enemies
- Detect laser hits
- Remove enemies with damage level above threshold 
- Add a scoring system 
- Detect game over (when at least one enemy reaches the bottom of the screen)
- "Game Over"-screen 
	- High Score Screen when a `newHighScoreEvent` event is detected
	- Game Over Screen otherwise
- Save highscore (the high score is simply saved in the textfile: `highscore.txt`)
- Add levels system ([read more about level system here](github.com/sondreandersen/space_invaders/levelSystem.md))
	- For every 1000 points - move up one level 
- Add multiple types of enemies:
	- Some with higher damage tolerance 
	- Make enemies with harder damage tolerance appear when the game progresses (i.e. higher levels are reached)

**TODO:**
- Update UML diagram
- Maybe add some limiation on how many shots can be fired for some unit of time - so to make the "spray and pray"-tactic less effective
- Enemies shooting back 


## Use this project 
Feel free to clone this reposetory, either to simply play the game or to add more functionallity to it! 


## Note
The UML-diagram has not been updated, and thus just provide an overview of the most basic functionallity of the game. I am planning on updating this diagram soon. 



