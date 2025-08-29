import simpleGE, random

from abc import ABCMeta, abstractmethod

from sprites.presets import *
from utils import ImageManip


class GameSprite(simpleGE.Sprite, metaclass=ABCMeta):
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

        self.movingRight = True
        self.flipped = False

        self.reset()
    
    def process(self) -> None:
        self.swim()
        self.resetIfNeeded()


    def resetIfNeeded(self) -> None:
        if self.needsReset():
            self.reset()

    def reset(self) -> None:
        self.applyRandomPreset()
        self.shufflePosition()

    @abstractmethod
    def needsReset(self) -> bool: ...

    @abstractmethod
    def applyRandomPreset(self) -> None: ...

    def applyPreset(self, preset: Preset) -> None:
        self.name = preset.name
        self.swimSpeed = random.randint(preset.speedMin, preset.speedMax)
        self.setImage(preset.imagePath)

        self.movingRight = random.randint(0, 1)
        self.flipped = False

        self.power = preset.power
        ImageManip.normalizeSizeToPower(self)
        ImageManip.flipIfNeeded(self)

    @abstractmethod
    def shufflePosition(self) -> None: ...

    @abstractmethod
    def swim(self) -> None: ...