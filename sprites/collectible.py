import random

from gameSprite import GameSprite
from sprites.presets import CollectiblePresets
from sprites.presets import PresetCollectible

class Collectible(GameSprite):

    def __init__(self, scene):
        super().__init__(scene)
        self.rotationIncrement = 0
        self.powerGain = 0

        self.reset()

    # override
    def reset(self):
        super().reset()
        self.rotationIncrement = random.randint(1, 5)
    
    def needsReset(self):
        return self.y >= self.screenHeight + self.BOUND_CONTINUE_THRESHOLD

    def applyRandomPreset(self):
        self.applyPreset(CollectiblePresets.randomPreset())

    # override
    def applyPreset(self, preset: PresetCollectible):
        super().applyPreset(preset)
        self.powerGain = preset.powerGain


    def shufflePosition(self):
        # self.y is multiplied for the illusion of seeming rarer than self actually is.
        self.y = -self.BOUND_CONTINUE_THRESHOLD * random.randint(1, 15)
        self.x = random.randint(0, self.screenHeight)

    def swim(self):
        self.turnBy(self.rotationIncrement)
        self.y += self.swimSpeed