from gameSprite import GameSprite
from presets import CrustaceanPresets

class Crustacean(GameSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.applyRandomPreset()

    def needsReset(self):
        pass

    def applyRandomPreset(self):
        self.applyPreset(CrustaceanPresets.randomPreset())

    def shufflePosition(self):
        pass

    def swim(self):
        pass