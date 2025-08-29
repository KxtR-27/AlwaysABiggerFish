import random

from gameSprite import GameSprite
from sprites.presets import *


class Fish(GameSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.applyRandomPreset()


    def needsReset(self):
        passedRightEdge = self.movingRight and self.x > self.screenWidth + Fish.FISH_CONTINUE_THRESHOLD
        passedLeftEdge = not self.movingRight and self.x < -Fish.FISH_CONTINUE_THRESHOLD

        return passedRightEdge or passedLeftEdge


    def applyRandomPreset(self):
        self.applyPreset(FishPresets.randomPreset())


    def shufflePosition(self) -> None:
        startFromLeft = random.randint(0, 1)

        self.x = -100 if startFromLeft else self.screenWidth + 100
        self.y = random.randint(0, self.screenHeight)

    def swim(self) -> None:
        direction = 1 if self.movingRight else -1
        self.x += self.swimSpeed * direction