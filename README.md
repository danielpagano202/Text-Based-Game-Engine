# Text-Based-Game-Engine
A game engine made in python which uses text as its graphic interface instead of regular 2d shapes and sprites.

## Features:
* Gameobjects made of multiple lines of text
* Movement of gameobjects eithe relative or globally
* Generation of each frame at any speed
* Gameobject flips and 90 degree rotations
* Deletion of game objects
* Deletion and replacemnt of individual characters in game objects
* Collision detection

## Uses of Engine:
* Platforms which only allow for text input
* Simple python console games

## Getting Started:
* Start by installing the project using **pip install textgameengine**
* To place your first object, run this code
```python
import textgameengine
#The stage is the area where all the gameobjects will go
stage = Stage(8, 8, ".")
#Text Assets are the equivalent of sprite assets in other game engines
textasset = TextAsset("^-^\n/|\\\n-^-")
#Stage.place places the textasset on to the stage at the coordinates
gameobject = stage.place(textasset, 2, 2, 0)
#Stage.print rebuilds the scene with any changes made to the stage and then prints it
stage.print()
```
* Let's say we want to move him to the right by one spot!
* To move a gameobject, you would use this code
 ```python
import textgameengine
#The stage is the area where all the gameobjects will go
stage = Stage(8, 8, ".")
#Text Assets are the equivalent of sprite assets in other game engines
textasset = TextAsset("^-^\n/|\\\n-^-")
#Stage.place places the textasset on to the stage at the coordinates
gameobject = stage.place(textasset, 2, 2, 0)
#Push moves the object relative to its position; In this case, it will move 1 unit to the right
gameobject.push(1, 0)
#Stage.print rebuilds the scene with any changes made to the stage and then prints it
stage.print()
```

