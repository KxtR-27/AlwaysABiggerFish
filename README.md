# Game Design Document
###### Kat R. | CS 439 - Game Engine Development
This project is for the "First Game" assignment in CS 439. 
The description website URL directs to the Canvas assignment page. 
If you have access, that is.

**This program requires the user to have `pygame` already installed.**

## Overview
Always A Bigger Fish is an arcade-style game in which the player controls a small fish. 
In the game are many other non-controlled fishes of varying sizes, as well as some other animals.
The player must eat fish that are smaller than them and avoid *being eaten* by fish *bigger* than them.

When the player eats (collides with and deletes) a smaller fish, their size increases slightly depending upon the size of what they ate.
Likewise, when the player is eaten (collides with and *gets* deleted), the game is immediately over.

The player's goal is to reach the biggest size they can within a 30-second\* round.
When the round is over--either by running out of time or by getting eaten--return to title screen.

###### \*subject to change.

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

| Asset                                                         | Attribution                                                                                                                    | Usage                                   |
|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <img src="assets/backdrop.png" width="100"><br>`backdrop.png` | [Image](https://craftpix.net/freebies/free-underwater-world-pixel-art-backgrounds/) from [Craftpix.net](https://craftpix.net/) | A background image for the game scenes. |
| <img src="assets/player.png" width="40"><br>`player.png`      | Icon made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](https://www.flaticon.com/)            | Icon used for Player Sprite.            |

## Milestones
### Satisfactory for Submission
<ol>
   <del>
      <li>Set up the In-game scene with a backdrop and a (not yet functional) Player Sprite.</li>
      <li>
         Player Sprite
         <ol>
            <li>Keyboard control</li>
            <li>Drifting motion behavior</li>
            <li>Custom boundary action to force away from edge</li>
         </ol>
      </li>
   </del>
   <li>
      BasicFish, and by extension, FishSprite
      <ol>
         <li>Create trigger for a Fish Sprite to despawn off-screen</li>
         <li>Make BasicFish move horizontally past the edge of the screen</li>
         <li>Spawn at random y-levels at regular intervals with a variable speed also applied</li>
      </ol>
   </li>
   <li>
      Fish Sprite collision logic
      <ol>
         <li>If player is bigger than the BasicFish, delete the BasicFish and increase player size</li>
         <li>If BasicFish is bigger, delete Player Sprite and trigger a game over</li>
         <li>Verify behavior with BasicFish</li>
      </ol>
   </li>
   <li>
      Add "presets" for BasicFish
      <ol>
         <li>An image, a speed range, and a size.</li>
         <li>Examples include a pufferfish, an orca, an angelfish, etc.</li>
         <li>Modify BasicFish spawning logic to randomly choose a preset</li>
      </ol>
   </li>
   <li>
      Create Bird presets mentioned in document
      <ol>
         <li>Extend Fish Sprite to use custom movement logic</li>
         <li>Make the Bird come in from the top, swoop into the water, and continue swoop up off the edge.</li>
         <li>Collision logic is handled by Fish Sprite</li>
         <li>Add random spawning mechanic</li>
      </ol>
   </li>
   <li>
      Create Crustacean presets mentioned in document
      <ol>
         <li>Extend Fish Sprite to use custom movement logic</li>
         <li>Make the crustacean scuttle in from the bottom edge, perhaps move sideways a short distance several times, and then scuttle back off the bottom edge.</li>
         <li>Collision logic is handled by Fish Sprite</li>
         <li>Add random spawning mechanic</li>
      </ol>
   </li>
   <li>
      Create Collectibles mentioned in document
      <ol>
         <li>Quite simply, move down from the top edge and despawn past the bottom edge</li>
         <li>Implement collision logic to increase player size</li>
         <li>Make them spawn rarely and at random x-positions</li>
      </ol>
   </li>
   <li>Add size and timer labels, complete with timer that exits the program when depleted</li>
   <li>Add size increase indicators</li>
   <li>
      Create Main Menu scene
      <ol>
         <li>Quit button to exit program</li>
         <li>Start button to run the In-game scene</li>
         <li>Best score and cause of death labels</li>
         <li>When the in-game scene ends, return size and cause of death to the Main Menu, which updates both values if this is a new best run</li>
      </ol>
   </li>
   <li>
      Animations
      <ol>
         <li>Make Player Sprite look in movement direction, flipping the image horizontally when the fish would look upside down</li>
         <li>
            Make Birds point in movement direction. 
            Using `moveAngle()` and `forward()` might be helpful here.
         </li>
         <li>Make collectibles slowly spin</li>
         <li>Make crustaceans rotate a little, back and forth, for a scuttling effect.</li>
      </ol>
   </li>
   <li>
      Sounds
      <ol>
         <li>Eating sound</li>
         <li>Collectible sound</li>
         <li>Button click sound</li>
         <li>Game over sound</li>
         <li>Ambient sounds?</li>
      </ol>
   </li>
   <li>TBD UI details</li>
</ol>

### Extra Ideas
1. Different fish presets have unique sounds
2. Weight the random preset algorithm to favor bigger fish as the player's size grows
3. Particle effects?
4. Game Over overlay in In-game scene. Lets players view the round's details before returning to Main Menu.
5. Joystick support
6. Stamina mechanic? (can sprint for short periods)

## Multi-State Considerations
The game runs the Main Menu scene. 
From here, the Main Menu can exit the program or begin an In-game scene. 
When the In-game scene exits, the Main Menu scene appears again.
This behavior will loop until the quit button is pressed.
