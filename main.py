import simpleGE

from fish import *
from player import Player


class GameScene(simpleGE.Scene):
    NUM_OF_NPC_FISHES = 10
    FISH_CONTINUE_TRESHOLD = 100
    PLAYER_GROWTH_FACTOR = 0.05

    def __init__(self, size=...):
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

    def process(self):
        for fish in self.fishes:
            self.runPlayerCollisionCheck(fish)
            self.resetIfNeeded(fish)

    def runPlayerCollisionCheck(self, fish: Fish):
        if fish.collidesWith(self.player) and not self.player.isInvincible():

            # print(f"Collision! [{self.player.name}: {self.player.power}] [{fish.name}: {fish.power}]")

            if fish.power >= self.player.power:
                exit(0)
            else:
                self.player.triggerIFrames()
                self.player.growBy(fish.power * GameScene.PLAYER_GROWTH_FACTOR)
                print(
                    f"[Player is now at {self.player.power} power] [Ate {fish.name} at {fish.power} power]"
                )
                fish.reset()

    def resetIfNeeded(self, fish: Fish):
        if self.fishHasPassedFarEdge(fish):
            fish.reset()

    def fishHasPassedFarEdge(self, fish: Fish):
        passedRightEdge = (
            fish.dx > 0 and fish.x > fish.screenWidth + GameScene.FISH_CONTINUE_TRESHOLD
        )
        passedLeftEdge = fish.dx < 0 and fish.x < -GameScene.FISH_CONTINUE_TRESHOLD

        return passedRightEdge or passedLeftEdge


def main():
    resolution = (960, 540)

    game = GameScene(resolution)
    game.start()


if __name__ == "__main__":
    main()
