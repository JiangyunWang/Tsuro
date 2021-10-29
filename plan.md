#Part 1
There are two identifiable components in our software system: an `automated player` and the `game software` in the server.
The server contains four classes: `Avatar`, `Tile`, `Player`, `Game`. 
 - `automated player`  has one piece: `Player`
 - `game software` has three pieces: `Avatar`, `Tile`, `Game`
### Tile
Tile is a square with 8 ports, 2 per side, and it specifies four distinct connections between two distinct ports; every 
port must have exactly one connection. A Tile records its own path and thecurrent position.

**Variables:**
- ``list: list_of_path``
- ``pair: position``
### Avatar
Avatar is a color token which should be one of the colors: ``white, black, red, green, blue``. It represents a player on
a port of one of the placed tiles. An Avatar stores its own color and its current position. Moreover,it records its own 
path. 

**Variables:**
- ``str: color``
- ``pair: <tile, dir_port> ``
   - ``pair: dir_port = <direction, n>``
   - ``str: direction (north, east, south, west)``
   - ``int: n (1,2)``
- ``list: list_of_pos``
### Automated player
Automated player is a play who chooses a tile and decides its position on the board and the start position of 
the ``Avatar``. Furthermore, it knows the whole process of the ``Game`` and sends its own decision of the next tile to the 
``Game``. Meanwhile, it gets the information from the ``Game`` that it wins or loses.

**Variables:**
- ``Avatar: avatar``
- ``boolean: lose``
### Game
`Game` starts Tsuro and assigns ``Avatars`` to its ``Players``. For each round, ``Player`` palces the `tile` on the 
 `board`, and `Game` updates `Avatars` according to the new added tile. After that it will check whether any `Player`
 loses the game. If yes, it removes the `Avator` and sends to the related `Player` that he/she loses the game. Otherwise, 
 continue play until someone wins.

**Variables:**
- ``list: list_of_Avatar``
- ``array[][]: board ``
- ``int: round``
