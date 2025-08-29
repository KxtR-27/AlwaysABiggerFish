import random
from enum import Enum


class Preset:
    def __init__(self, name: str, speedMin: float, speedMax: float, power: float, imagePath: str) -> None:
        self.name = name
        self.speedMin = speedMin
        self.speedMax = speedMax
        self.power = power
        self.imagePath = imagePath


PLAYER_PRESET = Preset("Player", speedMin=4, speedMax=4, power=30, imagePath="assets/player.png")


class FishPresets(Enum):
    BUTTERFLY = Preset(
        "Butterfly Fish", speedMin=2, speedMax=5, power=25, imagePath="assets/fish_butterfly.png",
    )
    SHARK = Preset(
        "Shark", speedMin=4, speedMax=8, power=100, imagePath="assets/fish_shark.png"
    )
    
    def randomPreset() -> Preset:
        return random.choice(list(FishPresets)).value