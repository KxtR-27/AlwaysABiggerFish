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
When the round is over--either by running out of time or by getting eaten--return to title screen.

[^1]: subject to change.

## List of Assets: Sprites
| Sprite Subclass          | Visual Elements                                                                                                                                                   | Animation Details                                                                                         | Lifespan                                                                | Movement                                                                                                                                              | Boundary Behavior             | Collision Behavior                                                                                                                                                            |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Player Sprite            | A goldfish, will stand out.                                                                                                                                       | Fish image will point in movement direction, flipping horizontally as needed.                             | Until time runs out, or when eaten                                      | WASD or arrow keys. Drifts to a stop if in motion with no keys pressed.                                                                               | STOP or BOUNCE (not yet sure) | If collides with any fish, a check is run to see whose size is bigger. The bigger grows and the smaller fish is deleted. If collides with any collectible, increase own size. |
| Fish Sprite              | Holds a value for an image and a size. Configured to despawn when offscreen. Configured for player collisions. Allows for more specific behaviors for subclasses. | As of now, none                                                                                           | Time needed to cross a boundary, or get eaten. Despawns off-screen.     | None                                                                                                                                                  | CONTINUE                      | Only if collides with player. A check is run to see whose size is bigger. The bigger grows and the smaller fish is deleted.                                                   |
| Fish Sprite > BasicFish  | Many "types" of fish use this. The "type" of fish is chosen randomly from a gallery of pictures. Each "type" has a corresponding size and speed range.            | Inherit                                                                                                   | Inherit                                                                 | BasicFish move in a horizontal line from one edge of the screen to another. They spawn at a random y-level. Speed range differs based on fish "type." | Inherit                       | Inherit                                                                                                                                                                       |
| Fish Sprite > Bird       | A seagull or a pelican. Have corresponding sizes.                                                                                                                 | Bird image will point in movement direction                                                               | Inherit                                                                 | Birds swoop down from the top of the screen, diving into the water before returning upward beyond the top edge.                                       | Inherit                       | Inherit                                                                                                                                                                       |
| Fish Sprite > Crustacean | A lobster, sea urchin, or crab. Corresponding sizes.                                                                                                              | When moving, rotates a little, ccw, before switching to cw, then ccw, then... imitates a sort of scuttle. | Inherit                                                                 | Scuttles up from bottom edge, waits, may or may not move sideways. Eventually returns downward beyond the bottom edge.                                | Inherit                       | Inherit                                                                                                                                                                       |
| Collectible              | A conch, clamshell, or a nautilus shell.                                                                                                                          | Slowly rotates in a randomly chosen direction                                                             | Time needed to cross a boundary, or get collected. Despawns off-screen. | Slowly moves downward from the top edge of the screen to the bottom edge.                                                                             | CONTINUE                      | If collides with player, player's size increases by a random value, no matter how small or big the player is. Despawns on contact.                                            |

## GUI Labels
| Scene     | Label             | Location                                                                | Appearance                                                                                  | Updates?                                                                                          |
|-----------|-------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Main Menu | Title             | Top-Middle of screen, translated up slightly.                           | "Always A Bigger Fish", in a bold, large font.                                              | None                                                                                              |
| Main Menu | Author            | Just below Title                                                        | "by Kat R. for CS 439 \"First Game\""                                                       | None                                                                                              |
| Main Menu | Best Size         | Middle or slightly bottom-middle of screen, below the Title and Author. | "Best Size: {size}", moderately large font size                                             | After each game ends, updated with player size from game if bigger than the previous value.       |
| Main Menu | Cause of Death    | Below Best Size                                                         | "Cause of Death: {cause}", smaller than best size                                           | When best size updates, Cause of Death updates as well with the loss condition of that best game. |
| In-game   | Size/Score        | Top middle, shifted left                                                | "Current Size: {size}" moderately-sized font, white text                                    | When the player fish eats another fish (and size changes)                                         |
| In-game   | Time Left         | Top middle, shifted right                                               | "Time left: {time left:.2f}" with same style as above                                       | Every frame, pulls from a timer                                                                   |
| In-game   | Size-Up Indicator | Instantiated at fish position on size increase                          | "+{size increase}" in small, black text. This text briefly floats upward before despawning. | Position updated every frame until despawn, but text never updates.                               |

## Other GUI Elements
| Scene     | Element      | Location                     | Appearance                             | Purpose                                                 |
|-----------|--------------|------------------------------|----------------------------------------|---------------------------------------------------------|
| Main Menu | Start Button | Bottom Middle, shifted left  | A rectangular button that says "Start" | Closes the Main Menu scene and opens the In-game scene. |
| Main Menu | Quit Button  | Bottom Middle, shifted right | A rectangular button that says "Quit"  | Closes the Main Menu scene and ends the program.        |

## Game/Scene Class Initialization
| Scene     | Appearance                                                                  | Sprites                                                                                                        | GUI Elements                                                      | Other Assets                                                                                                                                                                     |
|-----------|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main Menu | An underwater background with buttons and labels.                           | None                                                                                                           | 4 labels, 2 buttons. In class initialization.                     | Button click sound. In class init.                                                                                                                                               |
| In-game   | A different underwater background resembling a shallower area of the ocean. | Player, Fish, and Collectibles. Player in class init, fish and collectibles instantiated randomly during game. | 3 labels. 2 in class initialization, 1 instantiated on player eat | Timer, music, eat sound, collectible sound. Timer and music in class init. Eat sound instantiated for eat collisions; collectible sound instantiated for collectible collisions. |

## Game/Scene Class Behavior
| Scene     | Collision Management                                                                                                                                                                       | Sound Effect Triggers                                                                                                                     | Score & Timing Updates                                       | GUI Updates                                                                                          | Game End/Change Conditions                                                                                       |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Main Menu | None. No sprites.                                                                                                                                                                          | Both buttons have a sound trigger on click.                                                                                               | None. No scorekeeping or timer.                              | After each game, checks and/or updates best size and best cause of death.                            | Play button closes menu scene and transitions to in-game scene. Quit button closes menu scene and ends program.  |
| In-game   | Check for fish collision with player; on collision, affect player based on size. Check for collectible collision with player; always increases player size on collision. Runs every frame. | Fish-Player collision triggers eat sound. Collectible-Player collision triggers collectible sound. Ambient bubbling sounds play randomly. | Size score is updated on collision. Timer ticks every frame. | Score and timing updates reflect in labels. Any collision spawns an indicator that briefly despawns. | Game ends when either (1) the player fish is eaten for being too small, or (2) when the timer reaches 0.         |

## Asset List
Asset list will be updated as assets are added to the repo.
- All or most graphics come from [this Flaticon pack](https://www.flaticon.com/packs/ocean-34).
- All sounds come from [jsfxr](https://sfxr.me/).
- Background image is from [this 2D Background pack](https://craftpix.net/freebies/free-underwater-world-pixel-art-backgrounds/) on Craftpix.
- Music TBD.

| Asset | Attribution | Usage |
|-------|-------------|-------|
|       |             |       |

## Milestones
1. Set up the In-game scene with a backdrop and a (not yet functional) Player Sprite.
2. Implement keyboard controls to move the player sprite.
3. Enhance player sprite physics.
   i. Instead of stopping instantly when no keys are pressed, the sprite should drift to a stop.
   ii. Make the sprite's image face in the direction it is moving.
   iii. Flip the sprite horizontally when it would normally rotate upside-down
4. Implement a Fish Sprite
   i. Connect "size" used for eating
   ii. Set up Fish Sprite collisions with Player Sprite. Function can be empty.
   iii. Make Fish Sprites `CONTINUE` offscreen and despawn a short time after leaving it.
5. Implement a BasicFish
   i. Make it move sideways from either end of the screen across to the other end.
   ii. Confirm that it despawns after leaving the screen.
   iii. Go back to Fish Sprite and add collision code detailed in the Sprite List for "Collision Behavior"
6. Add more images and sizes to randomly initialize BasicFish to create variety.  
   -> A pufferfish, for example, which would be bigger than a minnow. Both are still BasicFish.

## Multi-State Considerations
...
