import random
from enum import Enum


class Preset:
    def __init__(
        self, name: str, speedMin: float, speedMax: float, power: float, imagePath: str
    ) -> None:
        self.name = name
        self.speedMin = speedMin
        self.speedMax = speedMax
        self.power = power
        self.imagePath = imagePath


PLAYER_PRESET = Preset(
    name="Player", speedMin=4, speedMax=4, power=40, imagePath="assets/player.png"
)


class FishPresets(Enum):
    BUTTERFLY = Preset(
        name="Butterfly Fish",
        speedMin=2,
        speedMax=5,
        power=25,
        imagePath="assets/fish_butterfly.png",
    )
    SHARK = Preset(
        name="Shark", 
        speedMin=4, 
        speedMax=8, 
        power=100, 
        imagePath="assets/fish_shark.png"
    )

    def randomPreset() -> Preset:
        return random.choice(list(FishPresets)).value

class BirdPresets(Enum):
    SEAGULL = Preset(
        name="Seagull",
        speedMin=3,
        speedMax=6,
        power=50,
        imagePath="assets/bird_seagull.png"
    )
    PELICAN = Preset(
        name="Pelican",
        speedMin=2,
        speedMax=4,
        power=60,
        imagePath="assets/bird_pelican.png"
    )

    def randomPreset() -> Preset:
        return random.choice(list(BirdPresets)).value

class CrustaceanPresets(Enum):
    CRAB = Preset(
        name="Crab",
        speedMin=3,
        speedMax=9,
        power=70,
        imagePath="assets/crustacean_crab.png"
    )
    LOBSTER = Preset(
        name="Lobster",
        speedMin=1,
        speedMax=3,
        power=90,
        imagePath="assets/crustacean_lobster.png"
    )
    SEA_URCHIN = Preset(
        name="Sea Urchin",
        speedMin=3,
        speedMax=7,
        power=40,
        imagePath="assets/crustacean_sea-urchin.png"
    )

    def randomPreset() -> Preset:
        return random.choice(list(CrustaceanPresets)).value