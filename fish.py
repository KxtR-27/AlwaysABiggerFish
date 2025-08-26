import simpleGE, random
from enum import Enum

class Preset:
    def __init__(self, name: str, speedMin: float, speedMax: float, power: float, imagePath: str):
        self.name = name
        self.speedMin = speedMin
        self.speedMax = speedMax
        self.power = power
        self.imagePath = imagePath

class FishPresets(Enum):
    # TODO: Crop icons to create more accurate hitboxes

    PLAYER =    Preset("Player", speedMin=4, speedMax=4, power=30, imagePath="assets/player.png")
    BUTTERFLY = Preset("Butterfly Fish", speedMin=2, speedMax=6, power=25, imagePath="assets/fish_butterfly.png")
    SHARK =     Preset("Shark", speedMin=4, speedMax=8, power=100, imagePath="assets/fish_shark.png")

    def randomFish():
        choice = random.choice(list(FishPresets))

        if choice is not FishPresets.PLAYER:
            return choice
        else:
            return FishPresets.randomFish()


class Fish(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setBoundAction(self.CONTINUE)

        # Placeholder values
        self.name = "Placeholder"
        self.swimSpeed = 0
        self.power = 0
        self.setImage("assets/placeholder.png")
        self.setSize(50, 50)

        self.reset()
    

    def reset(self):
        self.applyRandomPreset()
        self.shufflePosition()

    def applyRandomPreset(self):
        self.applyPreset(FishPresets.randomFish())
    
    def applyPreset(self, preset: FishPresets):
        preset = preset.value

        self.name = preset.name
        self.swimSpeed = random.randint(preset.speedMin, preset.speedMax)
        self.setImage(preset.imagePath)
        
        self.power = preset.power
        self.setSize(self.power, self.power)
    

    def shufflePosition(self):
        startFromLeft = random.randint(0, 1)

        self.x = -100 if startFromLeft else self.screenWidth + 100  
        self.y = random.randint(0, self.screenHeight)

        self.swim(startFromLeft)

    def swim(self, startFromLeft: bool):
        if startFromLeft:
            self.dx = self.swimSpeed
        else:
            self.dx = -self.swimSpeed