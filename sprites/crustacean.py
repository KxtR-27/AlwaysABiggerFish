import random, enum

from enum import Enum
from gameSprite import GameSprite
from sprites.presets import CrustaceanPresets


class Crustacean(GameSprite):
    class State(Enum):
        ASCENDING = enum.auto()
        STANDING = enum.auto()
        SCUTTLING = enum.auto()
        DESCENDING = enum.auto()
    
    CHANCE_TO_SCUTTLE = 0.03
    CHANCE_TO_DESCEND = 0.01
    MAX_SCUTTLE_SPEED_MULT = 1.2

    def __init__(self, scene):
        super().__init__(scene)

        self.state = None
        self.ascendingYTarget = 0

        self.scuttlingXTarget = 0
        self.scuttlingSpeed = 0

    def needsReset(self):
        return self.y > self.screenHeight + self.BOUND_CONTINUE_THRESHOLD

    def applyRandomPreset(self):
        self.applyPreset(CrustaceanPresets.randomPreset())

    def shufflePosition(self):
        self.y = self.screenHeight + self.BOUND_CONTINUE_THRESHOLD - 1
        self.x = random.randint(0, self.screenWidth)

        self.state = Crustacean.State.ASCENDING
        self.ascendingYTarget = self.screenHeight - random.randint(25, 100)

    def swim(self):
        match self.state:
            case Crustacean.State.ASCENDING:
                if self.y <= self.ascendingYTarget:
                    self.state = Crustacean.State.STANDING
                else:
                    self.y -= self.swimSpeed

            case Crustacean.State.STANDING:
                self._transitionFromStanding()

            case Crustacean.State.SCUTTLING:
                if self._scuttledFarEnough():
                    self.state = Crustacean.State.STANDING
                else:
                    self.x += self.scuttlingSpeed
                    
            case Crustacean.State.DESCENDING:
                self.y += self.swimSpeed


            case _:
                self.reset()
    

    def _transitionFromStanding(self):
        newState = Crustacean._calcStandingTransition()

        if newState is Crustacean.State.SCUTTLING:
            self.scuttlingXTarget = random.randint(50, self.screenWidth - 50)
            self.scuttlingSpeed = self.swimSpeed * (random.random() + 1 * Crustacean.MAX_SCUTTLE_SPEED_MULT)

            self.movingRight = self.x < self.scuttlingXTarget
            self.scuttlingSpeed *= 1 if self.movingRight else -1
        
        self.state = newState
    
    def _calcStandingTransition() -> State:
        adjustedScuttleChance = Crustacean.CHANCE_TO_SCUTTLE
        adjustedDescendChance = adjustedScuttleChance + Crustacean.CHANCE_TO_DESCEND

        outputPercentage = random.random() + 0.01 # starts at 1% chance instead of 0%

        if outputPercentage <= adjustedScuttleChance:
            return Crustacean.State.SCUTTLING
        elif outputPercentage <= adjustedDescendChance:
            return Crustacean.State.DESCENDING
        else:
            return Crustacean.State.STANDING


    def _scuttledFarEnough(self) -> bool:
        farEnoughRight = self.movingRight and self.x >= self.scuttlingXTarget
        farEnoughLeft = not self.movingRight and self.x <= self.scuttlingXTarget

        return farEnoughRight or farEnoughLeft