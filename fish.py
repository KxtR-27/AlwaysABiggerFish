import simpleGE, random

from presets import *
from utils import ImageManip


class Fish(simpleGE.Sprite):
    # how far off-screen can fish continue before resetting
    FISH_CONTINUE_THRESHOLD = 200

    def __init__(self, scene) -> None:
        super().__init__(scene)
        self.setBoundAction(self.CONTINUE)

        # Placeholder values
        self.name = "Placeholder"
        self.swimSpeed = 0
        self.power = 0
        self.setImage("assets/placeholder.png")
        self.setSize(50, 50)

        self.flipped = False

        self.reset()


    def reset(self):
        self.applyRandomPreset()
        self.shufflePosition()

    def resetIfNeeded(self):
        if self.hasPassedFarEdge():
            self.reset()

    def hasPassedFarEdge(self):
        passedRightEdge = (
            self.dx > 0 and self.x > self.screenWidth + Fish.FISH_CONTINUE_THRESHOLD
        )
        passedLeftEdge = self.dx < 0 and self.x < -Fish.FISH_CONTINUE_THRESHOLD

        return passedRightEdge or passedLeftEdge


    def applyRandomPreset(self):
        self.applyPreset(FishPresets.randomPreset())

    def applyPreset(self, preset: Preset) -> None:
        self.name = preset.name
        self.swimSpeed = random.randint(preset.speedMin, preset.speedMax)
        self.setImage(preset.imagePath)
        self.flipped = False

        self.power = preset.power
        ImageManip.normalizeSizeToPower(self)


    def shufflePosition(self) -> None:
        startFromLeft = random.randint(0, 1)

        self.x = -100 if startFromLeft else self.screenWidth + 100
        self.y = random.randint(0, self.screenHeight)

        self.swim(startFromLeft)

    def swim(self, startFromLeft: bool) -> None:
        if startFromLeft:
            self.dx = self.swimSpeed
            ImageManip.unflipFish(self)
        else:
            self.dx = -self.swimSpeed
            ImageManip.flipFish(self)
