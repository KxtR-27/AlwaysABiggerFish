import simpleGE

from fish import *
from player import Player

class GameScene(simpleGE.Scene):
    def __init__(self, size=...):
        super().__init__(size)

        self.setCaption("Eat smaller fish to get bigger!")
        self.setImage("assets/backdrop.png")

        self.player = Player(self)
        self.player.position = (self.player.screenWidth / 2, self.player.screenHeight / 2)

        self.fishes = []
        for _ in range(10):
            self.fishes.append(Fish(self))

        self.sprites = [
            self.player,
            self.fishes
        ]
    
    def process(self):
        for fish in self.fishes:
            self.runPlayerCollisionCheck(fish)
            self.resetIfNeeded(fish)
    
    def runPlayerCollisionCheck(self, fish: Fish):
        if fish.collidesWith(self.player):
            print(f"Collision! [{self.player.name}: {self.player.power}] [{fish.name}: {fish.power}]")
            if fish.power >= self.player.power:
                exit(0)
            else:
                fish.reset()
                self.player.increasePower(fish.power * 0.05)
    
    def resetIfNeeded(self, fish: Fish):
        if self.fishHasPassedFarEdge(fish):
            fish.reset()
        
    def fishHasPassedFarEdge(self, fish: Fish):
        return (fish.dx > 0 and fish.x > fish.screenWidth + 100) or (fish.dx < 0 and fish.x < -100)


def main():
    resolution = (960, 540)

    game = GameScene(resolution)
    game.start()

if __name__ == "__main__":
    main()