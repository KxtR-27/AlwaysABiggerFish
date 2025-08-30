import simpleGE

from sprites.fish import Fish
from sprites.bird import Bird
from sprites.player import Player


class GameScene(simpleGE.Scene):
    NUM_OF_FISHES = 10
    NUM_OF_BIRDS = 2
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

        self.sprites = [
            self.player, 
            self.fishes,
            self.birds
        ]

    def process(self) -> None:
        for fish in self.fishes:
            self.runPlayerCollisionCheck(fish)
        for bird in self.birds:
            self.runPlayerCollisionCheck(bird)
    

    def populateFishes(self) -> None:
        for _ in range (GameScene.NUM_OF_FISHES):
            self.fishes.append(Fish(self))

    def populateBirds(self) -> None:
        for _ in range (GameScene.NUM_OF_BIRDS):
            self.birds.append(Bird(self))


    def runPlayerCollisionCheck(self, animal: Fish | Bird) -> None:
        if animal.collidesWith(self.player):

            if animal.power > self.player.power and not self.player.isInvincible():
                exit(0)
            else:
                self.player.triggerIFrames()
                self.player.growBy(animal.power * GameScene.PLAYER_GROWTH_FACTOR)
                animal.reset()
