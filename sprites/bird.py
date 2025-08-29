import random

from gameSprite import GameSprite
from sprites.presets import BirdPresets
from utils import ImageManip

class Bird(GameSprite):
    ROTATION_INCREMENT = 0.5
    TURN_AFTER_Y = 0

    def __init__(self, scene):
        super().__init__(scene)
        self.applyRandomPreset()

    def needsReset(self) -> bool:
        return self.y < -GameSprite.BOUND_CONTINUE_THRESHOLD

    def applyRandomPreset(self) -> None:
        self.applyPreset(BirdPresets.randomPreset())

    def shufflePosition(self) -> None:
        self.x = random.randint(0, self.screenWidth)
        self.y = -GameSprite.BOUND_CONTINUE_THRESHOLD + 1
        
        self.setAngle(-90)

    def swim(self) -> None:
        rightMeansCCW = self.movingRight
        turnDirection = 1 if rightMeansCCW else -1

        if not self.moveAngle % 360 == 90 and self.y > Bird.TURN_AFTER_Y:
            self.turnBy(Bird.ROTATION_INCREMENT * turnDirection * self.swimSpeed)
        
        ImageManip.flipIfNeeded(self)
        self.forward(self.swimSpeed)