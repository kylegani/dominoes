## Dominoes Game
Dominoes is a family of games played with rectangular tiles. Each tile is divided into two square ends. Each end is marked with a number (one to
six) of spots or is blank. There are 28 tiles, one for each combination of spots and blanks.

## How It works:
- This is a two player game but for future sake, has been created with the addition of more players in mind.
- 28 tiles are shuffled face down and form the stock. Each player draws seven tiles.
- A random tile is added to the pile as the starting tile.
- The first player is chosen at random.
- The players alternately extend the line of play with one tile at one of its two ends.
- A tiles are added at either end provided that a player has a matching tile (including flipped tiles).
- If a player is unable to place a valid tile, they must keep on pulling tiles from the stock.
until they can.
- The game ends when one player wins by playing their last tile.

### Assumptions
- The players turn is ended when they pick up a tile.
- A stale mate (also known as a Milo) should never occur (this means that a combination of all tiles of one type are played with the value of this tile at both ends; thus preventing users from continuing play).


### Language choice
It is a common belief that applications built in the language most suited to the project is the best way to build software. Due to the algorithmic nature of this project, a language that is more geared toward processing and isolating data sets (with a proven performance track-record), Python, has been chosen.

### Decision Making algorithm
- Seeing as dominoes is a simple game with a first-to-finish objective, players play all their matching double tiles first.
- Players then play any blockers, which are tiles that match both ends, used to reduce the chances of an opponent having a tile available to play.
- Players then play their highest tallying and matching tile.
- Should users not have a tile to play, they draw a tile and their turn is ended.

## How to use this application:
### Running the application
- Python 3 is required to run this application and can be downloaded from https://www.python.org/downloads/
- The application can be run from the root directory using the following command:
```python3 main.py```
- The result of the game is printed directly to terminal.

### Running tests
- This application employs unit tests and can be run using the built-in unit testing library in the following way: 
```python3 -m unittest discover -v -s tests```
