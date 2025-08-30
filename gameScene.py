import simpleGE

from gameSprite import GameSprite
from sprites.player import Player
from sprites.fish import Fish
from sprites.bird import Bird
from sprites.crustacean import Crustacean
from sprites.collectible import Collectible


class GameScene(simpleGE.Scene):
    NUM_OF_FISHES = 10
    NUM_OF_BIRDS = 2
    NUM_OF_CRUSTACEANS = 3
    NUM_OF_COLLECTIBLES = 3

    PLAYER_GROWTH_FACTOR = 0.05

    def __init__(self, size=...) -> None:
        super().__init__(size)

        self.setCaption("Eat smaller fish to get bigger!")
        self.setImage("assets/backdrop.png")

        self.player = Player(self)
        self.player.triggerIFrames()
        self.player.position = (
            self.player.screenWidth / 2,
            self.player.screenHeight / 2,
        )

        self.fishes = []
        self.populateFishes()

        self.birds = []
        self.populateBirds()

        self.crustaceans = []
        self.populateCrustaceans()

        self.collectibles = []
        self.populateCollectibles()

        self.sprites = [
            self.player, 
            self.fishes,
            self.birds,
            self.crustaceans,
            self.collectibles
        ]

    def process(self) -> None:
        for fish in self.fishes:
            self.runPlayerCollisionCheck(fish)
        for bird in self.birds:
            self.runPlayerCollisionCheck(bird)
        for crustacean in self.crustaceans:
            self.runPlayerCollisionCheck(crustacean)
        for collectible in self.collectibles:
            self.runCollectibleCollisionCheck(collectible)
    

    def populateFishes(self) -> None:
        for _ in range (GameScene.NUM_OF_FISHES):
            self.fishes.append(Fish(self))

    def populateBirds(self) -> None:
        for _ in range (GameScene.NUM_OF_BIRDS):
            self.birds.append(Bird(self))
    
    def populateCrustaceans(self) -> None:
        for _ in range (GameScene.NUM_OF_CRUSTACEANS):
            self.crustaceans.append(Crustacean(self))
    
    def populateCollectibles(self) -> None:
        for _ in range (GameScene.NUM_OF_COLLECTIBLES):
            self.collectibles.append(Collectible(self))


    def runPlayerCollisionCheck(self, animal: Fish | Bird | Crustacean) -> None:
        if animal.collidesWith(self.player):

            if animal.power > self.player.power and not self.player.isInvincible():
                exit(0)
            else:
                self._playerEats(animal)

    def _playerEats(self, sprite: GameSprite):
        self.player.triggerIFrames()
        self.player.growBy(sprite.power * GameScene.PLAYER_GROWTH_FACTOR)
        sprite.reset()

    def runCollectibleCollisionCheck(self, collectible: Collectible):
        if collectible.collidesWith(self.player):
            self.player.triggerIFrames()
            self.player.growBy(collectible.powerGain)
            collectible.reset()