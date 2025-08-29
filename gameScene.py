import simpleGE

from sprites.fish import Fish
from sprites.player import Player


class GameScene(simpleGE.Scene):
    NUM_OF_NPC_FISHES = 10
    PLAYER_GROWTH_FACTOR = 0.05

    def __init__(self, size=...) -> None:
        super().__init__(size)

        self.setCaption("Eat smaller fish to get bigger!")
        self.setImage("assets/backdrop.png")

        self.player = Player(self)
        self.player.position = (
            self.player.screenWidth / 2,
            self.player.screenHeight / 2,
        )

        self.fishes = []

        for _ in range(GameScene.NUM_OF_NPC_FISHES):
            self.fishes.append(Fish(self))

        self.sprites = [self.player, self.fishes]

    def process(self) -> None:
        for fish in self.fishes:
            self.runPlayerCollisionCheck(fish)

    def runPlayerCollisionCheck(self, fish: Fish) -> None:
        if fish.collidesWith(self.player) and not self.player.isInvincible():
            
            if fish.power > self.player.power:
                exit(0)
            else:
                self.player.triggerIFrames()
                self.player.growBy(fish.power * GameScene.PLAYER_GROWTH_FACTOR)
                fish.reset()