# Python Tetris
Recreation of the game Tetris using Python by Taehyun Lee. I have always wanted to build a simple game on my own, and I thought that Tetris was a good start since it is one of the most popular game in the world and a very straightforward one. 
I do not offer any licenses for this project.
## How it is made
Pygame is used in this game to create controls and import assets easily. This game is made using a table of rows and columns. Each spaces contains information of the blocks and it displays the blocks based on that information on the screen by coloring them. 
For example, the spaces would be colored black as a black spot, white as a destined spot, and other colors as existing blocks. 
This game is heavily influenced by other Tetris-based games like tetr.io, and there are features that could be seen in those games such as combos, 7 bag, level, score, attacks (multiplayer) and more.
## Prerequisites
Pygame is required to run the game. To install Pygame, please type in the command prompt:
```
pip3 install pygame
```
After you have installed Pygame, run the game by typing:
```
py run.py
```
If the game is not running, please check the directory that you are in.
## Controls
More information can be found in the help section of the game. These are the keys that are being used:
### Single player
* Right, down, left arrows -> move block in that direction
* Up arrow -> rotate block
* Space -> place block
* Shift -> hold block
### Multi player
1P
* A, S, D -> move block in that direction
* W -> rotate block
* F -> place block
* Shift -> hold block

2P
* Right, down, left arrows -> move block in that direction
* Up arrow -> rotate block
* K -> place block
* L -> hold block
## In-game screenshots
![스크린샷 2024-10-14 211803](https://github.com/user-attachments/assets/b992d343-d1af-4cdb-846f-2685ecf8d497)
![스크린샷 2024-10-14 211828](https://github.com/user-attachments/assets/510441c9-f770-4492-a0e9-3c7393b7719f)
