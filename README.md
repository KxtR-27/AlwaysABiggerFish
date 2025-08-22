# Game Design Document
###### Kat R. | CS 439 - Game Engine Development
This project is for the "First Game" assignment in CS 439. 
The description website URL directs to the Canvas assignment page. 
If you have access, that is.

## Overview
Always A Bigger Fish is an arcade-style game in which the player controls a small fish. 
In the game are many other non-controlled fishes of varying sizes, as well as some other animals.
The player must eat fish that are smaller than them and avoid *being eaten* by fish *bigger* than them.

When the player eats (collides with and deletes) a smaller fish, their size increases slightly depending upon the size of what they ate.
Likewise, when the player is eaten (collides with and *gets* deleted), the game is immediately over.

The player's goal is to reach the biggest size they can within a 30-second[^1] round.

[^1]: subject to change.

## List of Assets
### Sprites
| Sprite Subclass | Visual Elements | Animation Details | Lifespan | Movement | Boundary Behavior | Collision Behavior |
|-----------------|-----------------|-------------------|----------|----------|-------------------|--------------------|
